// Copyright (c) Microsoft. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <iostream>
#include <cstdlib>
#include <atomic>
#include <Windows.h>

static LONG g_timerPeriodMs = 1000;
static DWORD g_totalDurationS = 5;
static LONGLONG g_busyPeriodMs = 100;

static std::atomic<bool> g_running{ true };

DWORD WINAPI TimerThreadProc(LPVOID lpParam)
{
    HANDLE hTimer = static_cast<HANDLE>(lpParam);
    DWORD tickCount = 0;

    LARGE_INTEGER freq;
    QueryPerformanceFrequency(&freq);
    LONGLONG countsPerBusyPeriod = freq.QuadPart * g_busyPeriodMs / 1000;

    while (g_running.load())
    {
        DWORD waitResult = WaitForSingleObject(hTimer, INFINITE);
        if (waitResult == WAIT_OBJECT_0)
        {
            if (!g_running.load())
                break;

            ++tickCount;

            LARGE_INTEGER start, current;
            QueryPerformanceCounter(&start);
            LONGLONG iterations = 0;

            do
            {
                QueryPerformanceCounter(&current);
                ++iterations;
            } while ((current.QuadPart - start.QuadPart) < countsPerBusyPeriod);
        }
        else
        {
            std::cerr << "WaitForSingleObject failed (" << GetLastError() << ")" << std::endl;
            break;
        }
    }

    return 0;
}

int main(int argc, char* argv[])
{
    if (argc != 4)
    {
        std::cerr << "Usage: " << argv[0]
                  << " <timer_period_ms> <busy_period_ms> <total_duration_s>"
                  << std::endl;
        return 1;
    }

    g_timerPeriodMs  = static_cast<LONG>(std::strtol(argv[1], nullptr, 10));
    g_busyPeriodMs   = static_cast<LONGLONG>(std::strtoll(argv[2], nullptr, 10));
    g_totalDurationS = static_cast<DWORD>(std::strtoul(argv[3], nullptr, 10));

    if (g_timerPeriodMs <= 0 || g_busyPeriodMs <= 0 || g_totalDurationS == 0)
    {
        std::cerr << "All arguments must be positive values." << std::endl;
        return 1;
    }

    HANDLE hTimer = CreateWaitableTimerExW(nullptr, nullptr, CREATE_WAITABLE_TIMER_HIGH_RESOLUTION, TIMER_ALL_ACCESS);
    if (!hTimer)
    {
        std::cerr << "CreateWaitableTimerEx failed (" << GetLastError() << ")" << std::endl;
        return 1;
    }

    LARGE_INTEGER dueTime;
    dueTime.QuadPart = -static_cast<LONGLONG>(g_timerPeriodMs) * 10000LL;

    if (!SetWaitableTimer(hTimer, &dueTime, g_timerPeriodMs, nullptr, nullptr, FALSE))
    {
        std::cerr << "SetWaitableTimer failed (" << GetLastError() << ")" << std::endl;
        CloseHandle(hTimer);
        return 1;
    }

    HANDLE hThread = CreateThread(nullptr, 0, TimerThreadProc, hTimer, 0, nullptr);
    if (!hThread)
    {
        std::cerr << "CreateThread failed (" << GetLastError() << ")" << std::endl;
        CancelWaitableTimer(hTimer);
        CloseHandle(hTimer);
        return 1;
    }

    Sleep(g_totalDurationS * 1000);

    g_running.store(false);
    CancelWaitableTimer(hTimer);

    // Set the timer to signal immediately so the thread wakes up and sees g_running == false.
    LARGE_INTEGER immediate;
    immediate.QuadPart = 0;
    SetWaitableTimer(hTimer, &immediate, 0, nullptr, nullptr, FALSE);

    WaitForSingleObject(hThread, INFINITE);

    CloseHandle(hThread);
    CloseHandle(hTimer);

    return 0;
}
