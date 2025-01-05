

<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="AI-generated website">
      <meta name="theme-color" content="#ffffff">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="robots" content="index, follow">
      
      <!-- Performance optimization: Preload critical resources -->
      <link rel="preload" href="https://cdn.tailwindcss.com" as="script">
      <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" as="style">
      
      <!-- Core CSS -->
      <script src="https://cdn.tailwindcss.com"></script>
      <script>
        tailwind.config = {
          theme: {
            extend: {
             colors: {
                primary: {
                  50: '#f8f8f8',
                  100: '#e8e8e8',
                  200: '#d3d3d3',
                  300: '#a3a3a3',
                  400: '#737373',
                  500: '#525252',
                  600: '#404040',
                  700: '#262626',
                  800: '#171717',
                  900: '#0a0a0a',
                  950: '#030303',
                },
                secondary: {
                  50: '#f8f8f8',
                  100: '#e8e8e8',
                  200: '#d3d3d3',
                  300: '#a3a3a3',
                  400: '#737373',
                  500: '#525252',
                  600: '#404040',
                  700: '#262626',
                  800: '#171717',
                  900: '#0a0a0a',
                  950: '#030303',
                },
                accent: {
                  50: '#f8f8f8',
                  100: '#e8e8e8',
                  200: '#d3d3d3',
                  300: '#a3a3a3',
                  400: '#737373',
                  500: '#525252',
                  600: '#404040',
                  700: '#262626',
                  800: '#171717',
                  900: '#0a0a0a',
                  950: '#030303',
                },
              },
              fontFamily: {
                sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
                heading: ['Montserrat', 'Inter', 'system-ui', 'sans-serif'],
              },
              spacing: {
                '18': '4.5rem',
                '22': '5.5rem',
                '30': '7.5rem',
              },
              maxWidth: {
                '8xl': '88rem',
                '9xl': '96rem',
              },
              animation: {
                'fade-in': 'fadeIn 0.5s ease-in',
                'fade-out': 'fadeOut 0.5s ease-out',
                'slide-up': 'slideUp 0.5s ease-out',
                'slide-down': 'slideDown 0.5s ease-out',
                'slide-left': 'slideLeft 0.5s ease-out',
                'slide-right': 'slideRight 0.5s ease-out',
                'scale-in': 'scaleIn 0.5s ease-out',
                'scale-out': 'scaleOut 0.5s ease-out',
                'spin-slow': 'spin 3s linear infinite',
                'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'bounce-slow': 'bounce 3s infinite',
                'float': 'float 3s ease-in-out infinite',
              },
              keyframes: {
                fadeIn: {
                  '0%': { opacity: '0' },
                  '100%': { opacity: '1' },
                },
                fadeOut: {
                  '0%': { opacity: '1' },
                  '100%': { opacity: '0' },
                },
                slideUp: {
                  '0%': { transform: 'translateY(20px)', opacity: '0' },
                  '100%': { transform: 'translateY(0)', opacity: '1' },
                },
                slideDown: {
                  '0%': { transform: 'translateY(-20px)', opacity: '0' },
                  '100%': { transform: 'translateY(0)', opacity: '1' },
                },
                slideLeft: {
                  '0%': { transform: 'translateX(20px)', opacity: '0' },
                  '100%': { transform: 'translateX(0)', opacity: '1' },
                },
                slideRight: {
                  '0%': { transform: 'translateX(-20px)', opacity: '0' },
                  '100%': { transform: 'translateX(0)', opacity: '1' },
                },
                scaleIn: {
                  '0%': { transform: 'scale(0.9)', opacity: '0' },
                  '100%': { transform: 'scale(1)', opacity: '1' },
                },
                scaleOut: {
                  '0%': { transform: 'scale(1.1)', opacity: '0' },
                  '100%': { transform: 'scale(1)', opacity: '1' },
                },
                float: {
                  '0%, 100%': { transform: 'translateY(0)' },
                  '50%': { transform: 'translateY(-10px)' },
                },
              },
              aspectRatio: {
                'portrait': '3/4',
                'landscape': '4/3',
                'ultrawide': '21/9',
              },
            },
          },
          variants: {
            extend: {
              opacity: ['disabled'],
              cursor: ['disabled'],
              backgroundColor: ['active', 'disabled'],
              textColor: ['active', 'disabled'],
            },
          },
        }
      </script>

      <!-- Utilities and Components -->
      <script defer src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.13.3/cdn.min.js"></script>
      <script defer src="https://cdnjs.cloudflare.com/ajax/libs/apexcharts/3.45.1/apexcharts.min.js"></script>
      
      <!-- Optimized Font Loading -->
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
      
      <!-- Icons -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" 
            integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
            crossorigin="anonymous" referrerpolicy="no-referrer" />

      <!-- Base Styles -->
      <style>

      * {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;     /* Firefox */
}

/* Webkit browsers like Chrome, Safari, newer Edge */
*::-webkit-scrollbar {
  display: none;
  width: 0;
  height: 0;
}
        /* Custom scrollbar */
        ::-webkit-scrollbar {
          width: 0px;
        }
        
        ::-webkit-scrollbar-track {
          background: #f1f1f1;
          border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
          background: #888;
          border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
          background: #666;
        }

        /* Remove tap highlight on mobile */
        * {
          -webkit-tap-highlight-color: transparent;
        }

        /* Improve text rendering */
        body {
          text-rendering: optimizeLegibility;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

        /* Focus outline styles */
        :focus-visible {
          outline: 2px solid currentColor;
          outline-offset: 2px;
        }

        /* Print styles */
        @media print {
          .no-print {
            display: none !important;
          }
          
          a[href]:after {
            content: " (" attr(href) ")";
          }
        }
      </style>

      <!-- Enhanced Image Handler -->
      <script>
        document.addEventListener('DOMContentLoaded', () => {
          const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
              if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                  const tempImage = new Image();
                  tempImage.onload = () => {
                    img.src = img.dataset.src;
                    img.classList.remove('opacity-0');
                    img.classList.add('opacity-100');
                  };
                  tempImage.src = img.dataset.src;
                  img.removeAttribute('data-src');
                  observer.unobserve(img);
                }
              }
            });
          }, {
            rootMargin: '50px 0px',
            threshold: 0.01
          });

          const loadImage = (img) => {
            if ('loading' in HTMLImageElement.prototype) {
              img.loading = 'lazy';
            }
            
            img.classList.add('transition-opacity', 'duration-300', 'opacity-0');
            
            img.onerror = () => {
              const width = img.getAttribute('width') || img.clientWidth || 300;
              const height = img.getAttribute('height') || img.clientHeight || 200;
              img.src = `https://placehold.co/${width}x${height}/DEDEDE/555555?text=Image+Unavailable`;
              img.alt = 'Image unavailable';
              img.classList.remove('opacity-0');
              img.classList.add('opacity-100', 'error-image');
            };

            if (img.dataset.src) {
              imageObserver.observe(img);
            } else {
              img.classList.remove('opacity-0');
              img.classList.add('opacity-100');
            }
          };

          document.querySelectorAll('img[data-src], img:not([data-src])').forEach(loadImage);

          // Watch for dynamically added images
          new MutationObserver((mutations) => {
            mutations.forEach(mutation => {
              mutation.addedNodes.forEach(node => {
                if (node.nodeType === 1) {
                  if (node.tagName === 'IMG') {
                    loadImage(node);
                  }
                  node.querySelectorAll('img').forEach(loadImage);
                }
              });
            });
          }).observe(document.body, {
            childList: true,
            subtree: true
          });
        });

        // Performance monitoring
        if ('performance' in window && 'PerformanceObserver' in window) {
          // Create performance observer
          const observer = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            entries.forEach((entry) => {
              if (entry.entryType === 'largest-contentful-paint') {
                // console.log(`LCP: ${entry.startTime}ms`);
              }
              if (entry.entryType === 'first-input') {
                // console.log(`FID: ${entry.processingStart - entry.startTime}ms`);
              }
              if (entry.entryType === 'layout-shift') {
                // console.log(`CLS: ${entry.value}`);
              }
            });
          });

          // Observe performance metrics
          observer.observe({ entryTypes: ['largest-contentful-paint', 'first-input', 'layout-shift'] });

          // Log basic performance metrics
          window.addEventListener('load', () => {
            const timing = performance.getEntriesByType('navigation')[0];
            console.log({
              'DNS Lookup': timing.domainLookupEnd - timing.domainLookupStart,
              'TCP Connection': timing.connectEnd - timing.connectStart,
              'DOM Content Loaded': timing.domContentLoadedEventEnd - timing.navigationStart,
              'Page Load': timing.loadEventEnd - timing.navigationStart
            });
          });
        }

        // Handle offline/online status
        window.addEventListener('online', () => {
          document.body.classList.remove('offline');
          console.log('Connection restored');
        });
        
        window.addEventListener('offline', () => {
          document.body.classList.add('offline');
          console.log('Connection lost');
        });
      </script>
   </head>
   <body class="antialiased text-gray-800 min-h-screen flex flex-col">
      <!-- Skip to main content link for accessibility -->
      <a href="#main-content" 
         class="sr-only focus:not-sr-only focus:absolute focus:top-0 focus:left-0 focus:z-50 focus:p-4 focus:bg-white focus:text-black">
         Skip to main content
      </a>

      <!-- Header -->
      <header class="relative z-50 bg-white dark:bg-gray-900">
        <!-- Header content goes here -->
      </header>

      <!-- Main content area -->
      <main id="main-content" class="flex-1 relative ">
        <!-- Content will be injected here -->
      </main>

   </body>
</html><htmlCode>
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multipurpose Reservoir System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <style>
        [x-cloak] { display: none !important; }
        html {
            scroll-behavior: smooth;
        }
        .active {
            @apply bg-blue-900 text-white;
        }
        .nav-link:hover {
            @apply bg-blue-800 text-white transition-all duration-200;
        }
    </style>
</head>
<body class="bg-neutral-900 text-white">
    <div id="root" class="flex">
        <div x-data="{ isOpen: false }" class="relative">
            <nav class="fixed h-screen w-64 bg-neutral-800 border-r border-neutral-700 hidden lg:block">
                <div class="p-4 border-b border-neutral-700">
                    <h1 class="text-xl font-bold text-blue-500">Reservoir System</h1>
                </div>
                
                <div class="py-4">
                    <a href="#dashboard" class="nav-link active flex items-center px-4 py-3 text-gray-300">
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
                        </svg>
                        Dashboard
                    </a>
                    <a href="#predictions" class="nav-link flex items-center px-4 py-3 text-gray-300">
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                        </svg>
                        Predictions
                    </a>
                    <a href="#users" class="nav-link flex items-center px-4 py-3 text-gray-300">
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
                        </svg>
                        Users
                    </a>
                </div>

                <div class="absolute bottom-0 w-full border-t border-neutral-700 p-4">
                    <div class="flex items-center">
                        <img src="https://avatar.iran.liara.run/public" alt="Profile" class="w-10 h-10 rounded-full">
                        <div class="ml-3">
                            <p class="text-sm font-medium">Admin User</p>
                            <p class="text-xs text-gray-400">admin@reservoir.com</p>
                        </div>
                    </div>
                </div>
            </nav>

            <!-- Mobile menu button -->
            <button type="button" class="lg:hidden fixed top-4 right-4 bg-neutral-800 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" @click="isOpen = !isOpen" aria-controls="mobile-menu" :aria-expanded="isOpen">
                <svg x-show="!isOpen" class="h-6 w-6 text-white" x-cloak fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
                <svg x-show="isOpen" class="h-6 w-6 text-white" x-cloak fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>

            <!-- Mobile menu -->
            <div id="mobile-menu" x-show="isOpen" x-cloak
                class="lg:hidden fixed inset-0 bg-neutral-800/80 backdrop-blur-lg"
                x-transition:enter="transition ease-out duration-100 transform"
                x-transition:enter-start="opacity-0 scale-95"
                x-transition:enter-end="opacity-100 scale-100"
                x-transition:leave="transition ease-in duration-75 transform"
                x-transition:leave-start="opacity-100 scale-100"
                x-transition:leave-end="opacity-0 scale-95"
                @click.away="isOpen = false"
                @resize.window="if (window.innerWidth > 1024) isOpen = false">
                
                <div class="p-4">
                    <div class="flex flex-col space-y-3">
                        <a href="#dashboard" class="text-white px-4 py-3 rounded-lg hover:bg-blue-800">Dashboard</a>
                        <a href="#predictions" class="text-gray-300 px-4 py-3 rounded-lg hover:bg-blue-800">Predictions</a>
                        <a href="#users" class="text-gray-300 px-4 py-3 rounded-lg hover:bg-blue-800">Users</a>
                    </div>
                </div>
            </div>
        </div>

        <main class="flex-1 ml-0 lg:ml-64">
            <MountPoint>
<script>
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.nav-link');
    
    links.forEach(link => {
        link.addEventListener('click', function() {
            links.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Set active link based on hash
    function setActiveLink() {
        const hash = window.location.hash || '#dashboard';
        links.forEach(link => {
            if(link.getAttribute('href') === hash) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    window.addEventListener('hashchange', setActiveLink);
    setActiveLink();
});
</script><htmlCode>
<section id="auth" class="min-h-screen bg-neutral-900 flex items-center justify-center p-4">
    <div class="w-full max-w-md">
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-8">
            <div class="text-center mb-8">
                <h2 class="text-2xl font-bold text-blue-500 mb-2">Reservoir System</h2>
                <p class="text-neutral-400">Welcome back! Please sign in.</p>
            </div>

            <form class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-neutral-300 mb-2">Email Address</label>
                    <input 
                        type="email" 
                        class="w-full px-4 py-3 bg-neutral-900 border border-neutral-700 rounded-lg focus:outline-none focus:border-blue-500 text-white placeholder-neutral-500"
                        placeholder="Enter your email"
                        required
                    >
                </div>

                <div>
                    <label class="block text-sm font-medium text-neutral-300 mb-2">Password</label>
                    <input 
                        type="password" 
                        class="w-full px-4 py-3 bg-neutral-900 border border-neutral-700 rounded-lg focus:outline-none focus:border-blue-500 text-white placeholder-neutral-500"
                        placeholder="Enter your password"
                        required
                    >
                </div>

                <div class="flex items-center justify-between">
                    <div class="flex items-center">
                        <input 
                            type="checkbox" 
                            id="remember" 
                            class="h-4 w-4 bg-neutral-900 border-neutral-700 rounded focus:ring-blue-500"
                        >
                        <label for="remember" class="ml-2 text-sm text-neutral-400">Remember me</label>
                    </div>
                    <a href="#" class="text-sm text-blue-500 hover:text-blue-400">Forgot password?</a>
                </div>

                <button 
                    type="submit" 
                    class="w-full py-3 px-4 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200"
                >
                    Sign In
                </button>
            </form>

            <div class="mt-6 text-center">
                <p class="text-neutral-400 text-sm">
                    Don't have an account? 
                    <a href="#" class="text-blue-500 hover:text-blue-400 font-medium">Sign up</a>
                </p>
            </div>
        </div>

        <div class="mt-8 text-center text-neutral-400 text-sm">
            <p>Protected by advanced encryption</p>
            <div class="flex items-center justify-center mt-4 space-x-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                </svg>
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
            </div>
        </div>
    </div>
</section>
</htmlCode><htmlCode>
<section id="dashboard" class="bg-neutral-900 p-6">
    <!-- Header -->
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Reservoir System Dashboard</h1>
        <p class="text-neutral-400">Monitor and analyze water dam metrics in real-time</p>
    </header>

    <!-- Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <!-- Water Dam Prediction Card -->
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <div class="flex items-center justify-between mb-4">
                <h3 class="text-lg font-semibold text-white">Water Level Prediction</h3>
                <svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
            </div>
            <p class="text-neutral-400 mb-4">AI-powered predictions for water levels and flow rates over the next 24 hours.</p>
            <div class="h-48 bg-neutral-900 rounded-lg border border-neutral-700 p-4">
                <!-- Line Chart Placeholder -->
                <canvas id="waterLevelChart"></canvas>
            </div>
        </div>

        <!-- User Dashboard Card -->
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <div class="flex items-center justify-between mb-4">
                <h3 class="text-lg font-semibold text-white">User Activity</h3>
                <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
                </svg>
            </div>
            <p class="text-neutral-400 mb-4">Monitor system access and user engagement metrics.</p>
            <div class="h-48 bg-neutral-900 rounded-lg border border-neutral-700 p-4">
                <!-- Bar Chart Placeholder -->
                <canvas id="userActivityChart"></canvas>
            </div>
        </div>

        <!-- Crop & Hydropower Card -->
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <div class="flex items-center justify-between mb-4">
                <h3 class="text-lg font-semibold text-white">Resource Generation</h3>
                <svg class="w-6 h-6 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
            </div>
            <p class="text-neutral-400 mb-4">Track hydropower generation and crop irrigation statistics.</p>
            <div class="h-48 bg-neutral-900 rounded-lg border border-neutral-700 p-4">
                <!-- Pie Chart Placeholder -->
                <canvas id="resourceChart"></canvas>
            </div>
        </div>
    </div>

    <!-- Statistics Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <h4 class="text-sm text-neutral-400 mb-2">Current Water Level</h4>
            <p class="text-2xl font-bold text-white">85.3m</p>
            <span class="text-green-500 text-sm">↑ 2.4%</span>
        </div>
        
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <h4 class="text-sm text-neutral-400 mb-2">Hydropower Output</h4>
            <p class="text-2xl font-bold text-white">2.8 MW</p>
            <span class="text-red-500 text-sm">↓ 1.2%</span>
        </div>
        
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <h4 class="text-sm text-neutral-400 mb-2">Irrigated Area</h4>
            <p class="text-2xl font-bold text-white">1,234 ha</p>
            <span class="text-green-500 text-sm">↑ 3.7%</span>
        </div>
        
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <h4 class="text-sm text-neutral-400 mb-2">System Health</h4>
            <p class="text-2xl font-bold text-white">98%</p>
            <span class="text-green-500 text-sm">Optimal</span>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Line Chart
        new Chart(document.getElementById('waterLevelChart'), {
            type: 'line',
            data: {
                labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
                datasets: [{
                    label: 'Water Level (m)',
                    data: [82, 84, 83, 85, 86, 85],
                    borderColor: '#3b82f6',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    },
                    x: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    }
                }
            }
        });

        // Bar Chart
        new Chart(document.getElementById('userActivityChart'), {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Active Users',
                    data: [65, 59, 80, 81, 56, 55, 40],
                    backgroundColor: '#10b981'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    },
                    x: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    }
                }
            }
        });

        // Pie Chart
        new Chart(document.getElementById('resourceChart'), {
            type: 'pie',
            data: {
                labels: ['Hydropower', 'Irrigation', 'Reserve'],
                datasets: [{
                    data: [40, 35, 25],
                    backgroundColor: ['#eab308', '#3b82f6', '#ef4444']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#9ca3af'
                        }
                    }
                }
            }
        });
    </script>
</section>
</htmlCode><htmlCode>
<section id="predictions" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Predictions Analysis</h1>
        <p class="text-neutral-400">Advanced predictive analytics for reservoir management</p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <!-- Water Level Prediction Details -->
        <div class="col-span-1 lg:col-span-2">
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-4">Water Level Forecast</h3>
                <div class="h-[400px] bg-neutral-900 rounded-lg border border-neutral-700 p-4 mb-4">
                    <canvas id="waterLevelForecast"></canvas>
                </div>
                <div class="grid grid-cols-3 gap-4 mt-4">
                    <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                        <p class="text-sm text-neutral-400">24h Prediction</p>
                        <p class="text-xl font-bold text-white">87.2m</p>
                        <span class="text-green-500 text-sm">↑ 1.8m</span>
                    </div>
                    <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                        <p class="text-sm text-neutral-400">48h Prediction</p>
                        <p class="text-xl font-bold text-white">88.5m</p>
                        <span class="text-green-500 text-sm">↑ 1.3m</span>
                    </div>
                    <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                        <p class="text-sm text-neutral-400">72h Prediction</p>
                        <p class="text-xl font-bold text-white">86.9m</p>
                        <span class="text-red-500 text-sm">↓ 1.6m</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Risk Assessment -->
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Risk Assessment</h3>
            <div class="space-y-4">
                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-neutral-400">Flood Risk</span>
                        <span class="text-green-500">Low</span>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2">
                        <div class="bg-green-500 h-2 rounded-full" style="width: 15%"></div>
                    </div>
                </div>

                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-neutral-400">Drought Risk</span>
                        <span class="text-yellow-500">Medium</span>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2">
                        <div class="bg-yellow-500 h-2 rounded-full" style="width: 45%"></div>
                    </div>
                </div>

                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-neutral-400">Structural Risk</span>
                        <span class="text-green-500">Low</span>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2">
                        <div class="bg-green-500 h-2 rounded-full" style="width: 10%"></div>
                    </div>
                </div>
            </div>

            <div class="mt-6">
                <h4 class="text-white font-semibold mb-3">Recent Alerts</h4>
                <div class="space-y-3">
                    <div class="flex items-center text-sm">
                        <span class="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                        <span class="text-neutral-400">Normal water flow detected</span>
                    </div>
                    <div class="flex items-center text-sm">
                        <span class="w-2 h-2 bg-yellow-500 rounded-full mr-2"></span>
                        <span class="text-neutral-400">Maintenance check scheduled</span>
                    </div>
                    <div class="flex items-center text-sm">
                        <span class="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                        <span class="text-neutral-400">Reservoir levels stable</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Weather Impact -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
        <h3 class="text-lg font-semibold text-white mb-4">Weather Impact Analysis</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                <p class="text-sm text-neutral-400 mb-1">Precipitation</p>
                <p class="text-xl font-bold text-white">32mm</p>
                <p class="text-sm text-blue-500">Expected in 24h</p>
            </div>
            <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                <p class="text-sm text-neutral-400 mb-1">Temperature</p>
                <p class="text-xl font-bold text-white">24°C</p>
                <p class="text-sm text-yellow-500">Above Average</p>
            </div>
            <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                <p class="text-sm text-neutral-400 mb-1">Wind Speed</p>
                <p class="text-xl font-bold text-white">15 km/h</p>
                <p class="text-sm text-green-500">Normal</p>
            </div>
            <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                <p class="text-sm text-neutral-400 mb-1">Humidity</p>
                <p class="text-xl font-bold text-white">65%</p>
                <p class="text-sm text-green-500">Optimal</p>
            </div>
        </div>
    </div>

    <script>
        // Water Level Forecast Chart
        new Chart(document.getElementById('waterLevelForecast'), {
            type: 'line',
            data: {
                labels: ['Now', '6h', '12h', '18h', '24h', '30h', '36h', '42h', '48h'],
                datasets: [{
                    label: 'Predicted Level',
                    data: [85.4, 86.1, 86.8, 87.2, 87.5, 88.0, 88.5, 87.8, 86.9],
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Safe Range',
                    data: [84, 84, 84, 84, 84, 84, 84, 84, 84],
                    borderColor: '#10b981',
                    borderDash: [5, 5],
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: '#9ca3af'
                        }
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    },
                    x: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    }
                }
            }
        });
    </script>
</section>
</htmlCode><htmlCode>
<section id="user-management" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <div class="flex justify-between items-center">
            <div>
                <h1 class="text-2xl font-bold text-white mb-2">User Management</h1>
                <p class="text-neutral-400">Manage system users and access controls</p>
            </div>
            <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                </svg>
                Add User
            </button>
        </div>
    </header>

    <!-- Search and Filter Bar -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4 mb-6">
        <div class="flex flex-col md:flex-row gap-4">
            <div class="flex-1">
                <input type="search" placeholder="Search users..." class="w-full bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
            </div>
            <div class="flex gap-4">
                <select class="bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
                    <option>All Roles</option>
                    <option>Admin</option>
                    <option>Engineer</option>
                    <option>Analyst</option>
                </select>
                <select class="bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
                    <option>All Status</option>
                    <option>Active</option>
                    <option>Inactive</option>
                </select>
            </div>
        </div>
    </div>

    <!-- Users Table -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg overflow-hidden">
        <table class="w-full">
            <thead class="bg-neutral-900">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">User</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Role</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Status</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Last Active</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Actions</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-neutral-700">
                <tr>
                    <td class="px-6 py-4">
                        <div class="flex items-center">
                            <img src="https://avatar.iran.liara.run/public" alt="User" class="w-8 h-8 rounded-full">
                            <div class="ml-4">
                                <div class="text-sm font-medium text-white">John Doe</div>
                                <div class="text-sm text-neutral-400">john@example.com</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 text-sm text-white">Admin</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Active</span>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">2 minutes ago</td>
                    <td class="px-6 py-4 text-sm">
                        <button class="text-blue-500 hover:text-blue-400 mr-3">Edit</button>
                        <button class="text-red-500 hover:text-red-400">Delete</button>
                    </td>
                </tr>
                <tr>
                    <td class="px-6 py-4">
                        <div class="flex items-center">
                            <img src="https://avatar.iran.liara.run/public" alt="User" class="w-8 h-8 rounded-full">
                            <div class="ml-4">
                                <div class="text-sm font-medium text-white">Jane Smith</div>
                                <div class="text-sm text-neutral-400">jane@example.com</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 text-sm text-white">Engineer</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Active</span>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">5 hours ago</td>
                    <td class="px-6 py-4 text-sm">
                        <button class="text-blue-500 hover:text-blue-400 mr-3">Edit</button>
                        <button class="text-red-500 hover:text-red-400">Delete</button>
                    </td>
                </tr>
                <tr>
                    <td class="px-6 py-4">
                        <div class="flex items-center">
                            <img src="https://avatar.iran.liara.run/public" alt="User" class="w-8 h-8 rounded-full">
                            <div class="ml-4">
                                <div class="text-sm font-medium text-white">Mike Johnson</div>
                                <div class="text-sm text-neutral-400">mike@example.com</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 py-4 text-sm text-white">Analyst</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-neutral-100 text-neutral-800">Inactive</span>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">2 days ago</td>
                    <td class="px-6 py-4 text-sm">
                        <button class="text-blue-500 hover:text-blue-400 mr-3">Edit</button>
                        <button class="text-red-500 hover:text-red-400">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Pagination -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg mt-6 p-4">
        <div class="flex items-center justify-between">
            <div class="text-neutral-400 text-sm">
                Showing 1 to 3 of 12 entries
            </div>
            <div class="flex space-x-2">
                <button class="px-3 py-1 rounded-lg bg-neutral-900 text-neutral-400 border border-neutral-700 hover:bg-neutral-700">Previous</button>
                <button class="px-3 py-1 rounded-lg bg-blue-600 text-white">1</button>
                <button class="px-3 py-1 rounded-lg bg-neutral-900 text-neutral-400 border border-neutral-700 hover:bg-neutral-700">2</button>
                <button class="px-3 py-1 rounded-lg bg-neutral-900 text-neutral-400 border border-neutral-700 hover:bg-neutral-700">3</button>
                <button class="px-3 py-1 rounded-lg bg-neutral-900 text-neutral-400 border border-neutral-700 hover:bg-neutral-700">Next</button>
            </div>
        </div>
    </div>
</section>
</htmlCode><htmlCode>
<section id="crop-analytics" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Crop Analytics & Predictions</h1>
        <p class="text-neutral-400">Monitor and analyze crop yields based on reservoir data</p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <!-- Main Analytics Chart -->
        <div class="lg:col-span-2 bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <div class="flex justify-between items-center mb-6">
                <h3 class="text-lg font-semibold text-white">Seasonal Crop Yield Prediction</h3>
                <select class="bg-neutral-900 border border-neutral-700 rounded-lg px-3 py-2 text-white text-sm">
                    <option>Last 6 Months</option>
                    <option>Last Year</option>
                    <option>All Time</option>
                </select>
            </div>
            <div class="h-[400px] bg-neutral-900 rounded-lg border border-neutral-700 p-4">
                <canvas id="cropYieldChart"></canvas>
            </div>
        </div>

        <!-- Irrigation Stats -->
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Irrigation Statistics</h3>
            <div class="space-y-4">
                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <p class="text-sm text-neutral-400 mb-1">Current Water Usage</p>
                    <div class="flex items-end justify-between">
                        <p class="text-2xl font-bold text-white">2,450</p>
                        <p class="text-sm text-green-500">m³/hour</p>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2 mt-2">
                        <div class="bg-blue-500 h-2 rounded-full" style="width: 75%"></div>
                    </div>
                </div>

                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <p class="text-sm text-neutral-400 mb-1">Irrigation Efficiency</p>
                    <div class="flex items-end justify-between">
                        <p class="text-2xl font-bold text-white">92%</p>
                        <p class="text-sm text-green-500">Optimal</p>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2 mt-2">
                        <div class="bg-green-500 h-2 rounded-full" style="width: 92%"></div>
                    </div>
                </div>

                <div class="bg-neutral-900 p-4 rounded-lg border border-neutral-700">
                    <p class="text-sm text-neutral-400 mb-1">Soil Moisture</p>
                    <div class="flex items-end justify-between">
                        <p class="text-2xl font-bold text-white">78%</p>
                        <p class="text-sm text-yellow-500">Normal</p>
                    </div>
                    <div class="w-full bg-neutral-700 rounded-full h-2 mt-2">
                        <div class="bg-yellow-500 h-2 rounded-full" style="width: 78%"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Crop Distribution -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Crop Distribution</h3>
            <div class="h-[300px]">
                <canvas id="cropDistributionChart"></canvas>
            </div>
        </div>

        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Water Allocation by Crop</h3>
            <div class="h-[300px]">
                <canvas id="waterAllocationChart"></canvas>
            </div>
        </div>
    </div>

    <!-- Key Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <p class="text-sm text-neutral-400">Total Irrigated Area</p>
            <p class="text-2xl font-bold text-white mt-1">12,450 ha</p>
            <p class="text-sm text-green-500 mt-1">↑ 3.2% vs last month</p>
        </div>
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <p class="text-sm text-neutral-400">Expected Yield</p>
            <p class="text-2xl font-bold text-white mt-1">4.8 tons/ha</p>
            <p class="text-sm text-green-500 mt-1">↑ 2.1% vs last season</p>
        </div>
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <p class="text-sm text-neutral-400">Water Efficiency</p>
            <p class="text-2xl font-bold text-white mt-1">89%</p>
            <p class="text-sm text-yellow-500 mt-1">← Maintained</p>
        </div>
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-4">
            <p class="text-sm text-neutral-400">Crop Health Index</p>
            <p class="text-2xl font-bold text-white mt-1">8.4/10</p>
            <p class="text-sm text-green-500 mt-1">↑ 0.3 vs last week</p>
        </div>
    </div>

    <script>
        // Crop Yield Chart
        new Chart(document.getElementById('cropYieldChart'), {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Actual Yield',
                    data: [4.2, 4.4, 4.5, 4.6, 4.7, 4.8],
                    borderColor: '#3b82f6',
                    tension: 0.4
                },
                {
                    label: 'Predicted Yield',
                    data: [4.2, 4.4, 4.5, 4.6, 4.8, 5.0],
                    borderColor: '#10b981',
                    borderDash: [5, 5],
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { color: '#9ca3af' }
                    }
                },
                scales: {
                    y: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    },
                    x: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    }
                }
            }
        });

        // Crop Distribution Chart
        new Chart(document.getElementById('cropDistributionChart'), {
            type: 'pie',
            data: {
                labels: ['Rice', 'Wheat', 'Corn', 'Soybeans', 'Others'],
                datasets: [{
                    data: [30, 25, 20, 15, 10],
                    backgroundColor: ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: { color: '#9ca3af' }
                    }
                }
            }
        });

        // Water Allocation Chart
        new Chart(document.getElementById('waterAllocationChart'), {
            type: 'bar',
            data: {
                labels: ['Rice', 'Wheat', 'Corn', 'Soybeans', 'Others'],
                datasets: [{
                    label: 'Water Usage (m³/ha)',
                    data: [1200, 800, 600, 500, 300],
                    backgroundColor: '#3b82f6'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { color: '#9ca3af' }
                    }
                },
                scales: {
                    y: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    },
                    x: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    }
                }
            }
        });
    </script>
</section>
</htmlCode><htmlCode>
<section id="reports" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">System Reports</h1>
        <p class="text-neutral-400">Comprehensive reports and analytics for reservoir management</p>
    </header>

    <!-- Report Generation Tools -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6 mb-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <label class="block text-sm font-medium text-neutral-400 mb-2">Report Type</label>
                <select class="w-full bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
                    <option>Water Level Analysis</option>
                    <option>Power Generation Report</option>
                    <option>Irrigation Statistics</option>
                    <option>System Performance</option>
                </select>
            </div>
            <div>
                <label class="block text-sm font-medium text-neutral-400 mb-2">Time Period</label>
                <select class="w-full bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
                    <option>Last 7 Days</option>
                    <option>Last 30 Days</option>
                    <option>Last Quarter</option>
                    <option>Custom Range</option>
                </select>
            </div>
            <div>
                <label class="block text-sm font-medium text-neutral-400 mb-2">Format</label>
                <select class="w-full bg-neutral-900 border border-neutral-700 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500">
                    <option>PDF Report</option>
                    <option>Excel Sheet</option>
                    <option>CSV Export</option>
                </select>
            </div>
        </div>
        <div class="mt-6 flex justify-end">
            <button class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg flex items-center">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                </svg>
                Generate Report
            </button>
        </div>
    </div>

    <!-- Recent Reports -->
    <div class="bg-neutral-800 border border-neutral-700 rounded-lg overflow-hidden mb-8">
        <div class="p-6 border-b border-neutral-700">
            <h3 class="text-lg font-semibold text-white">Recent Reports</h3>
        </div>
        <table class="w-full">
            <thead class="bg-neutral-900">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Report Name</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Generated On</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Type</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Status</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-neutral-400 uppercase tracking-wider">Actions</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-neutral-700">
                <tr class="hover:bg-neutral-850">
                    <td class="px-6 py-4">
                        <div class="text-sm font-medium text-white">Monthly Performance Review</div>
                        <div class="text-sm text-neutral-400">June 2023</div>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">2023-06-30 15:30</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800">PDF</span>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Completed</span>
                    </td>
                    <td class="px-6 py-4 text-sm space-x-3">
                        <button class="text-blue-500 hover:text-blue-400">Download</button>
                        <button class="text-neutral-400 hover:text-neutral-300">Share</button>
                    </td>
                </tr>
                <tr class="hover:bg-neutral-850">
                    <td class="px-6 py-4">
                        <div class="text-sm font-medium text-white">Water Level Analysis</div>
                        <div class="text-sm text-neutral-400">Q2 2023</div>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">2023-06-15 09:45</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Excel</span>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Completed</span>
                    </td>
                    <td class="px-6 py-4 text-sm space-x-3">
                        <button class="text-blue-500 hover:text-blue-400">Download</button>
                        <button class="text-neutral-400 hover:text-neutral-300">Share</button>
                    </td>
                </tr>
                <tr class="hover:bg-neutral-850">
                    <td class="px-6 py-4">
                        <div class="text-sm font-medium text-white">Power Generation Stats</div>
                        <div class="text-sm text-neutral-400">May 2023</div>
                    </td>
                    <td class="px-6 py-4 text-sm text-neutral-400">2023-05-31 17:20</td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">CSV</span>
                    </td>
                    <td class="px-6 py-4">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">Completed</span>
                    </td>
                    <td class="px-6 py-4 text-sm space-x-3">
                        <button class="text-blue-500 hover:text-blue-400">Download</button>
                        <button class="text-neutral-400 hover:text-neutral-300">Share</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Report Analytics -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Report Generation Statistics</h3>
            <div class="h-[300px]">
                <canvas id="reportsChart"></canvas>
            </div>
        </div>
        <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
            <h3 class="text-lg font-semibold text-white mb-4">Most Requested Reports</h3>
            <div class="h-[300px]">
                <canvas id="reportTypesChart"></canvas>
            </div>
        </div>
    </div>

    <script>
        // Reports Generation Chart
        new Chart(document.getElementById('reportsChart'), {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Reports Generated',
                    data: [65, 78, 82, 75, 90, 85],
                    borderColor: '#3b82f6',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { color: '#9ca3af' }
                    }
                },
                scales: {
                    y: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    },
                    x: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    }
                }
            }
        });

        // Report Types Chart
        new Chart(document.getElementById('reportTypesChart'), {
            type: 'doughnut',
            data: {
                labels: ['Water Level', 'Power Generation', 'Irrigation', 'System Performance'],
                datasets: [{
                    data: [35, 25, 20, 20],
                    backgroundColor: ['#3b82f6', '#10b981', '#f59e0b', '#ef4444']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: { color: '#9ca3af' }
                    }
                }
            }
        });
    </script>
</section>
</htmlCode><htmlCode>
<section id="settings" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">System Settings</h1>
        <p class="text-neutral-400">Configure your reservoir management system preferences</p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Main Settings Column -->
        <div class="lg:col-span-2 space-y-6">
            <!-- Profile Settings -->
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-6">Profile Settings</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Full Name</label>
                        <input type="text" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500" value="John Doe">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Email Address</label>
                        <input type="email" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500" value="john@reservoir.com">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Phone Number</label>
                        <input type="tel" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500" value="+1 234 567 8900">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Role</label>
                        <input type="text" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500" value="System Administrator" disabled>
                    </div>
                </div>
            </div>

            <!-- Notification Settings -->
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-6">Notification Preferences</h3>
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h4 class="text-white">Water Level Alerts</h4>
                            <p class="text-sm text-neutral-400">Get notified when water levels reach critical points</p>
                        </div>
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" class="sr-only peer" checked>
                            <div class="w-11 h-6 bg-neutral-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                        </label>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <h4 class="text-white">System Reports</h4>
                            <p class="text-sm text-neutral-400">Receive weekly performance reports</p>
                        </div>
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" class="sr-only peer" checked>
                            <div class="w-11 h-6 bg-neutral-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                        </label>
                    </div>
                    <div class="flex items-center justify-between">
                        <div>
                            <h4 class="text-white">Maintenance Updates</h4>
                            <p class="text-sm text-neutral-400">Get notified about system maintenance</p>
                        </div>
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" class="sr-only peer">
                            <div class="w-11 h-6 bg-neutral-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                        </label>
                    </div>
                </div>
            </div>

            <!-- System Preferences -->
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-6">System Preferences</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Time Zone</label>
                        <select class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500">
                            <option>UTC-05:00 Eastern Time</option>
                            <option>UTC+00:00 GMT</option>
                            <option>UTC+01:00 Central European Time</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Date Format</label>
                        <select class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500">
                            <option>MM/DD/YYYY</option>
                            <option>DD/MM/YYYY</option>
                            <option>YYYY-MM-DD</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

        <!-- Security Settings -->
        <div class="space-y-6">
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-6">Security Settings</h3>
                <div class="space-y-6">
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Current Password</label>
                        <input type="password" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">New Password</label>
                        <input type="password" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-neutral-400 mb-2">Confirm New Password</label>
                        <input type="password" class="w-full px-4 py-2 bg-neutral-900 border border-neutral-700 rounded-lg text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <button class="w-full bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition duration-200">
                            Update Password
                        </button>
                    </div>
                </div>
            </div>

            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-6">Two-Factor Authentication</h3>
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h4 class="text-white">Enable 2FA</h4>
                        <p class="text-sm text-neutral-400">Secure your account with 2FA</p>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                        <input type="checkbox" class="sr-only peer">
                        <div class="w-11 h-6 bg-neutral-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                    </label>
                </div>
            </div>
        </div>
    </div>

    <!-- Save Changes Button -->
    <div class="mt-8 flex justify-end">
        <button class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg transition duration-200">
            Save Changes
        </button>
    </div>
</section>
</htmlCode><htmlCode>
<section id="profile" class="bg-neutral-900 p-6">
    <header class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">User Profile</h1>
        <p class="text-neutral-400">Manage your account and view activity</p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Profile Card -->
        <div class="lg:col-span-1">
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <div class="text-center">
                    <img src="https://avatar.iran.liara.run/public" alt="Profile" class="w-32 h-32 rounded-full mx-auto mb-4">
                    <h2 class="text-xl font-bold text-white">John Doe</h2>
                    <p class="text-neutral-400">System Administrator</p>
                    <div class="mt-4 flex justify-center space-x-2">
                        <span class="px-3 py-1 bg-blue-600 text-white text-sm rounded-full">Admin</span>
                        <span class="px-3 py-1 bg-green-600 text-white text-sm rounded-full">Active</span>
                    </div>
                </div>
                <div class="mt-6 border-t border-neutral-700 pt-6">
                    <div class="text-sm text-neutral-400">
                        <div class="flex items-center mb-3">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                            </svg>
                            john@reservoir.com
                        </div>
                        <div class="flex items-center mb-3">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                            </svg>
                            +1 234 567 8900
                        </div>
                        <div class="flex items-center">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                            </svg>
                            New York, USA
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="lg:col-span-3 space-y-6">
            <!-- Activity Stats -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                    <div class="flex items-center justify-between">
                        <h3 class="text-lg font-semibold text-white">Total Logins</h3>
                        <span class="text-2xl font-bold text-blue-500">247</span>
                    </div>
                    <p class="text-sm text-neutral-400 mt-2">Last login: 2 hours ago</p>
                </div>
                <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                    <div class="flex items-center justify-between">
                        <h3 class="text-lg font-semibold text-white">Reports Generated</h3>
                        <span class="text-2xl font-bold text-green-500">123</span>
                    </div>
                    <p class="text-sm text-neutral-400 mt-2">Last report: Today</p>
                </div>
                <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                    <div class="flex items-center justify-between">
                        <h3 class="text-lg font-semibold text-white">Actions Taken</h3>
                        <span class="text-2xl font-bold text-yellow-500">589</span>
                    </div>
                    <p class="text-sm text-neutral-400 mt-2">Last action: 5 mins ago</p>
                </div>
            </div>

            <!-- Recent Activity -->
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-4">Recent Activity</h3>
                <div class="space-y-4">
                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center">
                                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <p class="text-white">Generated Monthly Report</p>
                            <p class="text-sm text-neutral-400">2 hours ago</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="w-8 h-8 rounded-full bg-green-600 flex items-center justify-center">
                                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <p class="text-white">Reviewed Water Level Data</p>
                            <p class="text-sm text-neutral-400">5 hours ago</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0">
                            <div class="w-8 h-8 rounded-full bg-yellow-600 flex items-center justify-center">
                                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                                </svg>
                            </div>
                        </div>
                        <div class="ml-4">
                            <p class="text-white">Updated System Parameters</p>
                            <p class="text-sm text-neutral-400">Yesterday</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Activity Chart -->
            <div class="bg-neutral-800 border border-neutral-700 rounded-lg p-6">
                <h3 class="text-lg font-semibold text-white mb-4">Activity Overview</h3>
                <div class="h-64">
                    <canvas id="activityChart"></canvas>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Activity Chart
        new Chart(document.getElementById('activityChart'), {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Activity Level',
                    data: [65, 59, 80, 81, 56, 55, 40],
                    fill: true,
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    },
                    x: {
                        grid: {
                            color: '#374151'
                        },
                        ticks: {
                            color: '#9ca3af'
                        }
                    }
                }
            }
        });
    </script>
</section>
</htmlCode>
