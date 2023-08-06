// Copyright 2016-2017 Francesco Biscani (bluescarni@gmail.com)
//
// This file is part of the mp++ library.
//
// This Source Code Form is subject to the terms of the Mozilla
// Public License v. 2.0. If a copy of the MPL was not distributed
// with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

#ifndef MPPP_CONFIG_HPP
#define MPPP_CONFIG_HPP

// Start of defines instantiated by CMake.
// clang-format off
#define MPPP_VERSION 0.5
#define MPPP_VERSION_MAJOR 0
#define MPPP_VERSION_MINOR 5


// clang-format on
// End of defines instantiated by CMake.

// Compiler configuration.

// NOTE: check for MSVC first, as clang-cl does define both __clang__ and _MSC_VER,
// and we want to configure it as MSVC.
#if defined(_MSC_VER)

// clang-cl supports __builtin_expect().
#if defined(__clang__)
#define mppp_likely(x) __builtin_expect(!!(x), 1)
#define mppp_unlikely(x) __builtin_expect(!!(x), 0)
#else
#define mppp_likely(x) (x)
#define mppp_unlikely(x) (x)
#endif
#define MPPP_RESTRICT __restrict

#elif defined(__clang__) || defined(__GNUC__) || defined(__INTEL_COMPILER)

#define mppp_likely(x) __builtin_expect(!!(x), 1)
#define mppp_unlikely(x) __builtin_expect(!!(x), 0)
#define MPPP_RESTRICT __restrict

#else

#define mppp_likely(x) (x)
#define mppp_unlikely(x) (x)
#define MPPP_RESTRICT

#endif

// thread_local configuration.
#if defined(__apple_build_version__) || defined(__MINGW32__) || defined(__INTEL_COMPILER)

// - Apple clang does not support the thread_local keyword until very recent versions.
// - Testing shows that at least some MinGW versions have buggy thread_local implementations.
// - Also on Intel the thread_local keyword looks buggy.
#define MPPP_MAYBE_TLS

#else

// For the rest, we assume thread_local is available.
#define MPPP_MAYBE_TLS static thread_local
#define MPPP_HAVE_THREAD_LOCAL

#endif

// Concepts setup.
#if defined(__cpp_concepts)

#define MPPP_HAVE_CONCEPTS

#endif

// C++ standard setup.
// NOTE: this is necessary because at this time MSVC does not set correctly the
// __cplusplus macro.
#if defined(_MSC_VER)

#define MPPP_CPLUSPLUS _MSVC_LANG

#else

#define MPPP_CPLUSPLUS __cplusplus

#endif

// constexpr setup.
#if MPPP_CPLUSPLUS >= 201402L

#define MPPP_CONSTEXPR_14 constexpr

#else

#define MPPP_CONSTEXPR_14

#endif

#endif
