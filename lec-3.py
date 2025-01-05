
landing
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
<div id="root">
  <nav id="navbar" class="fixed w-full z-50 backdrop-blur-lg bg-neutral-900/80 border-b border-neutral-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex-shrink-0">
          <a href="#" class="text-white font-bold text-xl">MRS</a>
        </div>
        
        <div class="hidden md:block">
          <div class="ml-10 flex items-center space-x-8">
            <a href="#" class="text-neutral-300 hover:text-white px-3 py-2 text-sm font-medium transition-colors">Home</a>
            <a href="#" class="text-neutral-300 hover:text-white px-3 py-2 text-sm font-medium transition-colors">About</a>
            <a href="#" class="text-neutral-300 hover:text-white px-3 py-2 text-sm font-medium transition-colors">Services</a>
            <a href="#" class="text-neutral-300 hover:text-white px-3 py-2 text-sm font-medium transition-colors">Contact</a>
            <button class="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition-colors">
              Get Started
            </button>
          </div>
        </div>

        <div class="md:hidden">
          <button id="menuBtn" class="text-neutral-300 hover:text-white">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div id="mobileMenu" class="hidden md:hidden bg-neutral-900/95 backdrop-blur-lg">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <a href="#" class="text-neutral-300 hover:text-white block px-3 py-2 text-base font-medium animate__animated animate__fadeInDown">Home</a>
        <a href="#" class="text-neutral-300 hover:text-white block px-3 py-2 text-base font-medium animate__animated animate__fadeInDown animate__delay-1s">About</a>
        <a href="#" class="text-neutral-300 hover:text-white block px-3 py-2 text-base font-medium animate__animated animate__fadeInDown animate__delay-2s">Services</a>
        <a href="#" class="text-neutral-300 hover:text-white block px-3 py-2 text-base font-medium animate__animated animate__fadeInDown animate__delay-3s">Contact</a>
        <button class="w-full bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition-colors mt-4 animate__animated animate__fadeInUp animate__delay-4s">
          Get Started
        </button>
      </div>
    </div>
  </nav>

  <script>
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    let isMenuOpen = false;

    menuBtn.addEventListener('click', () => {
      isMenuOpen = !isMenuOpen;
      if (isMenuOpen) {
        mobileMenu.classList.remove('hidden');
        menuBtn.innerHTML = `
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        `;
      } else {
        mobileMenu.classList.add('hidden');
        menuBtn.innerHTML = `
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        `;
      }
    });

    // Close mobile menu on window resize
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 768) {
        mobileMenu.classList.add('hidden');
        isMenuOpen = false;
        menuBtn.innerHTML = `
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        `;
      }
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="hero" class="min-h-[70vh] bg-neutral-900 relative overflow-hidden pt-20">
    <!-- Gradient Background -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-purple-600/20"></div>
    
    <!-- Glassmorphism Circles -->
    <div class="absolute top-20 left-20 w-72 h-72 bg-indigo-600/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-20 right-20 w-72 h-72 bg-purple-600/10 rounded-full blur-3xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <div class="flex flex-col lg:flex-row items-center justify-between pt-20">
        <div class="w-full lg:w-1/2 text-center lg:text-left mb-12 lg:mb-0">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6 animate__animated animate__fadeInUp">
            Multipurpose Reservoir System
          </h1>
          <p class="text-lg text-neutral-300 mb-8 animate__animated animate__fadeInUp animate__delay-1s">
            Advanced water management solution for sustainable resource utilization and efficient distribution across multiple sectors.
          </p>
          <div class="flex flex-wrap gap-4 justify-center lg:justify-start animate__animated animate__fadeInUp animate__delay-2s">
            <button class="px-8 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors backdrop-blur-sm">
              Get Started
            </button>
            <button class="px-8 py-3 border border-neutral-500 text-white rounded-lg hover:bg-white/10 transition-colors backdrop-blur-sm">
              Learn More
            </button>
          </div>
        </div>

        <div class="w-full lg:w-1/2 relative animate__animated animate__fadeInRight">
          <div class="relative z-10 backdrop-blur-lg bg-white/5 p-4 rounded-2xl border border-neutral-800">
            <img src="https://avatar.iran.liara.run/public" alt="Reservoir System" class="w-full h-auto rounded-lg"/>
            <div class="absolute -inset-1 bg-gradient-to-r from-indigo-600/20 to-purple-600/20 rounded-2xl blur"></div>
          </div>
        </div>
      </div>

      <!-- Stats Section -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mt-20 pb-12">
        <div class="backdrop-blur-lg bg-white/5 p-6 rounded-xl border border-neutral-800 animate__animated animate__fadeInUp">
          <h3 class="text-3xl font-bold text-white mb-2">98%</h3>
          <p class="text-neutral-400">Efficiency Rate</p>
        </div>
        <div class="backdrop-blur-lg bg-white/5 p-6 rounded-xl border border-neutral-800 animate__animated animate__fadeInUp animate__delay-1s">
          <h3 class="text-3xl font-bold text-white mb-2">50+</h3>
          <p class="text-neutral-400">Active Systems</p>
        </div>
        <div class="backdrop-blur-lg bg-white/5 p-6 rounded-xl border border-neutral-800 animate__animated animate__fadeInUp animate__delay-2s">
          <h3 class="text-3xl font-bold text-white mb-2">24/7</h3>
          <p class="text-neutral-400">Monitoring</p>
        </div>
        <div class="backdrop-blur-lg bg-white/5 p-6 rounded-xl border border-neutral-800 animate__animated animate__fadeInUp animate__delay-3s">
          <h3 class="text-3xl font-bold text-white mb-2">1M+</h3>
          <p class="text-neutral-400">Users Served</p>
        </div>
      </div>
    </div>
  </section>

  <script>
    // Scroll Animation
    window.addEventListener('scroll', () => {
      const stats = document.querySelectorAll('.animate__animated');
      stats.forEach(stat => {
        const rect = stat.getBoundingClientRect();
        const isVisible = rect.top <= window.innerHeight * 0.75;
        if (isVisible) {
          stat.style.visibility = 'visible';
          stat.classList.add('animate__fadeInUp');
        }
      });
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="features" class="py-20 bg-neutral-800">
    <!-- Background Elements -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/5 to-purple-600/5"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Key Features</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Advanced capabilities designed to revolutionize water resource management and distribution
        </p>
      </div>

      <!-- Features Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Feature 1 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp">
          <div class="h-12 w-12 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">Real-time Monitoring</h3>
          <p class="text-neutral-300">Advanced sensors and analytics for continuous water level and quality monitoring.</p>
        </div>

        <!-- Feature 2 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-1s">
          <div class="h-12 w-12 bg-purple-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">Automated Control</h3>
          <p class="text-neutral-300">Smart distribution systems with AI-powered decision making capabilities.</p>
        </div>

        <!-- Feature 3 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-2s">
          <div class="h-12 w-12 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">Data Analytics</h3>
          <p class="text-neutral-300">Comprehensive reporting and predictive analysis for optimal resource management.</p>
        </div>

        <!-- Feature 4 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp">
          <div class="h-12 w-12 bg-purple-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">24/7 Operation</h3>
          <p class="text-neutral-300">Continuous system operation with redundant backup systems for reliability.</p>
        </div>

        <!-- Feature 5 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-1s">
          <div class="h-12 w-12 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">Scalable Infrastructure</h3>
          <p class="text-neutral-300">Modular design allowing easy expansion and integration with existing systems.</p>
        </div>

        <!-- Feature 6 -->
        <div class="group backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-2s">
          <div class="h-12 w-12 bg-purple-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-white mb-3">Advanced Security</h3>
          <p class="text-neutral-300">Multi-layer security protocols protecting both physical and digital assets.</p>
        </div>
      </div>
    </div>
  </section>

  <script>
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      observer.observe(element);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="services" class="py-20 bg-neutral-900 relative">
    <!-- Gradient Background -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Our Services</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Comprehensive water management solutions tailored to your needs
        </p>
      </div>

      <!-- Services Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Service Card 1 -->
        <div class="group relative backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden hover:translate-y-[-5px] transition-all duration-300 animate__animated animate__fadeInUp">
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          <div class="p-8 relative">
            <div class="h-14 w-14 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-4">Water Distribution</h3>
            <p class="text-neutral-300 mb-6">Efficient and automated water distribution systems with real-time monitoring and control.</p>
            <a href="#" class="inline-flex items-center text-indigo-400 hover:text-indigo-300 transition-colors">
              Learn more
              <svg class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Service Card 2 -->
        <div class="group relative backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden hover:translate-y-[-5px] transition-all duration-300 animate__animated animate__fadeInUp animate__delay-1s">
          <div class="absolute inset-0 bg-gradient-to-br from-purple-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          <div class="p-8 relative">
            <div class="h-14 w-14 bg-purple-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-4">Quality Control</h3>
            <p class="text-neutral-300 mb-6">Advanced monitoring systems ensuring water quality meets the highest standards.</p>
            <a href="#" class="inline-flex items-center text-purple-400 hover:text-purple-300 transition-colors">
              Learn more
              <svg class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Service Card 3 -->
        <div class="group relative backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden hover:translate-y-[-5px] transition-all duration-300 animate__animated animate__fadeInUp animate__delay-2s">
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          <div class="p-8 relative">
            <div class="h-14 w-14 bg-indigo-600/20 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <svg class="w-8 h-8 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-4">Resource Optimization</h3>
            <p class="text-neutral-300 mb-6">Smart algorithms for optimal resource allocation and utilization efficiency.</p>
            <a href="#" class="inline-flex items-center text-indigo-400 hover:text-indigo-300 transition-colors">
              Learn more
              <svg class="w-4 h-4 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      observer.observe(element);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="portfolio" class="py-20 bg-neutral-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Our Portfolio</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Explore our successful implementations and innovative solutions
        </p>
      </div>

      <!-- Portfolio Filter -->
      <div class="flex flex-wrap justify-center gap-4 mb-12 animate__animated animate__fadeInUp">
        <button class="px-6 py-2 rounded-full bg-indigo-600 text-white hover:bg-indigo-700 transition-colors">All</button>
        <button class="px-6 py-2 rounded-full bg-white/5 text-white hover:bg-white/10 transition-colors backdrop-blur-sm">Reservoirs</button>
        <button class="px-6 py-2 rounded-full bg-white/5 text-white hover:bg-white/10 transition-colors backdrop-blur-sm">Distribution</button>
        <button class="px-6 py-2 rounded-full bg-white/5 text-white hover:bg-white/10 transition-colors backdrop-blur-sm">Monitoring</button>
      </div>

      <!-- Portfolio Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Portfolio Item 1 -->
        <div class="group relative backdrop-blur-lg bg-white/5 rounded-xl overflow-hidden animate__animated animate__fadeInUp">
          <div class="relative overflow-hidden">
            <img src="https://avatar.iran.liara.run/public" alt="Project 1" class="w-full h-64 object-cover transform group-hover:scale-110 transition-transform duration-500"/>
            <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity duration-300 flex items-end">
              <div class="p-6">
                <h3 class="text-xl font-semibold text-white mb-2">Smart Reservoir System</h3>
                <p class="text-neutral-300">Advanced monitoring and control system implementation</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Portfolio Item 2 -->
        <div class="group relative backdrop-blur-lg bg-white/5 rounded-xl overflow-hidden animate__animated animate__fadeInUp animate__delay-1s">
          <div class="relative overflow-hidden">
            <img src="https://avatar.iran.liara.run/public" alt="Project 2" class="w-full h-64 object-cover transform group-hover:scale-110 transition-transform duration-500"/>
            <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity duration-300 flex items-end">
              <div class="p-6">
                <h3 class="text-xl font-semibold text-white mb-2">Distribution Network</h3>
                <p class="text-neutral-300">Efficient water distribution system deployment</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Portfolio Item 3 -->
        <div class="group relative backdrop-blur-lg bg-white/5 rounded-xl overflow-hidden animate__animated animate__fadeInUp animate__delay-2s">
          <div class="relative overflow-hidden">
            <img src="https://avatar.iran.liara.run/public" alt="Project 3" class="w-full h-64 object-cover transform group-hover:scale-110 transition-transform duration-500"/>
            <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity duration-300 flex items-end">
              <div class="p-6">
                <h3 class="text-xl font-semibold text-white mb-2">Quality Monitoring</h3>
                <p class="text-neutral-300">Real-time water quality analysis system</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- View More Button -->
      <div class="text-center mt-12">
        <button class="px-8 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors animate__animated animate__fadeInUp">
          View More Projects
        </button>
      </div>
    </div>
  </section>

  <script>
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      observer.observe(element);
    });

    // Portfolio Filter Animation
    const filterButtons = document.querySelectorAll('#portfolio button');
    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        filterButtons.forEach(btn => btn.classList.remove('bg-indigo-600'));
        this.classList.add('bg-indigo-600');
      });
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="testimonials" class="py-20 bg-neutral-900 relative overflow-hidden">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>
    <div class="absolute -top-40 -right-40 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl"></div>
    <div class="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-600/10 rounded-full blur-3xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Client Testimonials</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          What our clients say about our reservoir management solutions
        </p>
      </div>

      <!-- Testimonials Slider -->
      <div class="testimonial-slider relative">
        <div class="overflow-hidden">
          <div class="flex transition-transform duration-500" id="testimonialTrack">
            <!-- Testimonial 1 -->
            <div class="w-full md:w-1/2 lg:w-1/3 flex-shrink-0 px-4">
              <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-8 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp">
                <div class="flex items-center mb-6">
                  <img src="https://avatar.iran.liara.run/public" alt="Client" class="w-12 h-12 rounded-full object-cover"/>
                  <div class="ml-4">
                    <h4 class="text-white font-semibold">John Smith</h4>
                    <p class="text-neutral-400">Water Resource Manager</p>
                  </div>
                </div>
                <p class="text-neutral-300 mb-6">
                  "The implementation of this system has revolutionized how we manage our water resources. Efficiency has improved by 45%."
                </p>
                <div class="flex text-yellow-400">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
              </div>
            </div>

            <!-- Testimonial 2 -->
            <div class="w-full md:w-1/2 lg:w-1/3 flex-shrink-0 px-4">
              <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-8 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-1s">
                <div class="flex items-center mb-6">
                  <img src="https://avatar.iran.liara.run/public" alt="Client" class="w-12 h-12 rounded-full object-cover"/>
                  <div class="ml-4">
                    <h4 class="text-white font-semibold">Sarah Johnson</h4>
                    <p class="text-neutral-400">Operations Director</p>
                  </div>
                </div>
                <p class="text-neutral-300 mb-6">
                  "The real-time monitoring capabilities have transformed our decision-making process. Highly recommended!"
                </p>
                <div class="flex text-yellow-400">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
              </div>
            </div>

            <!-- Testimonial 3 -->
            <div class="w-full md:w-1/2 lg:w-1/3 flex-shrink-0 px-4">
              <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-8 hover:bg-white/10 transition-all duration-300 animate__animated animate__fadeInUp animate__delay-2s">
                <div class="flex items-center mb-6">
                  <img src="https://avatar.iran.liara.run/public" alt="Client" class="w-12 h-12 rounded-full object-cover"/>
                  <div class="ml-4">
                    <h4 class="text-white font-semibold">Michael Brown</h4>
                    <p class="text-neutral-400">Project Manager</p>
                  </div>
                </div>
                <p class="text-neutral-300 mb-6">
                  "Outstanding support team and innovative solutions. Our reservoir management has never been more efficient."
                </p>
                <div class="flex text-yellow-400">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Navigation Buttons -->
        <button class="absolute top-1/2 -left-4 transform -translate-y-1/2 bg-indigo-600 p-2 rounded-full text-white hover:bg-indigo-700 transition-colors" id="prevBtn">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
        </button>
        <button class="absolute top-1/2 -right-4 transform -translate-y-1/2 bg-indigo-600 p-2 rounded-full text-white hover:bg-indigo-700 transition-colors" id="nextBtn">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
      </div>
    </div>
  </section>

  <script>
    const track = document.getElementById('testimonialTrack');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    let currentIndex = 0;
    const testimonials = track.children.length;

    function updateSlidePosition() {
      const slideWidth = track.children[0].offsetWidth + 32; // Width + gap
      track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }

    prevBtn.addEventListener('click', () => {
      currentIndex = Math.max(currentIndex - 1, 0);
      updateSlidePosition();
    });

    nextBtn.addEventListener('click', () => {
      currentIndex = Math.min(currentIndex + 1, testimonials - 1);
      updateSlidePosition();
    });

    // Update on window resize
    window.addEventListener('resize', updateSlidePosition);

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated', 'animate__fadeInUp');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      observer.observe(element);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="pricing" class="py-20 bg-neutral-800 relative overflow-hidden">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>
    <div class="absolute top-0 right-0 w-96 h-96 bg-indigo-600/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-purple-600/10 rounded-full blur-3xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Flexible Pricing Plans</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Choose the perfect plan that fits your water management needs
        </p>
      </div>

      <!-- Pricing Cards Container -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <!-- Basic Plan -->
        <div class="relative group animate__animated animate__fadeInUp">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-2xl p-8 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-2">
            <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl"></div>
            <div class="relative">
              <h3 class="text-xl font-semibold text-white mb-4">Basic Plan</h3>
              <div class="flex items-baseline mb-8">
                <span class="text-4xl font-bold text-white">$299</span>
                <span class="text-neutral-400 ml-2">/month</span>
              </div>
              <ul class="space-y-4 mb-8">
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Basic Monitoring System
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  5 Sensor Points
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Monthly Reports
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Email Support
                </li>
              </ul>
              <button class="w-full py-3 px-6 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition-colors">
                Get Started
              </button>
            </div>
          </div>
        </div>

        <!-- Pro Plan -->
        <div class="relative group animate__animated animate__fadeInUp animate__delay-1s">
          <div class="backdrop-blur-lg bg-white/5 border-2 border-indigo-500 rounded-2xl p-8 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-2">
            <div class="absolute -top-4 right-4 bg-indigo-500 text-white px-3 py-1 rounded-full text-sm">Popular</div>
            <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl"></div>
            <div class="relative">
              <h3 class="text-xl font-semibold text-white mb-4">Pro Plan</h3>
              <div class="flex items-baseline mb-8">
                <span class="text-4xl font-bold text-white">$599</span>
                <span class="text-neutral-400 ml-2">/month</span>
              </div>
              <ul class="space-y-4 mb-8">
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Advanced Monitoring
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  15 Sensor Points
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Weekly Reports
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  24/7 Support
                </li>
              </ul>
              <button class="w-full py-3 px-6 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition-colors">
                Get Started
              </button>
            </div>
          </div>
        </div>

        <!-- Enterprise Plan -->
        <div class="relative group animate__animated animate__fadeInUp animate__delay-2s">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-2xl p-8 hover:bg-white/10 transition-all duration-300 transform hover:-translate-y-2">
            <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity rounded-2xl"></div>
            <div class="relative">
              <h3 class="text-xl font-semibold text-white mb-4">Enterprise Plan</h3>
              <div class="flex items-baseline mb-8">
                <span class="text-4xl font-bold text-white">$999</span>
                <span class="text-neutral-400 ml-2">/month</span>
              </div>
              <ul class="space-y-4 mb-8">
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Full System Access
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Unlimited Sensors
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Real-time Reports
                </li>
                <li class="flex items-center text-neutral-300">
                  <svg class="w-5 h-5 text-indigo-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  Dedicated Support
                </li>
              </ul>
              <button class="w-full py-3 px-6 rounded-lg bg-indigo-600 text-white hover:bg-indigo-700 transition-colors">
                Contact Sales
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated');
          entry.target.style.visibility = 'visible';
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      element.style.visibility = 'hidden';
      observer.observe(element);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="team" class="py-20 bg-neutral-900 relative overflow-hidden">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>
    <div class="absolute top-40 right-0 w-72 h-72 bg-indigo-600/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-40 left-0 w-72 h-72 bg-purple-600/10 rounded-full blur-3xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Our Expert Team</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Meet the dedicated professionals behind our successful water management solutions
        </p>
      </div>

      <!-- Team Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- Team Member 1 -->
        <div class="group animate__animated animate__fadeInUp">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden transition-transform duration-300 transform hover:-translate-y-2">
            <div class="relative overflow-hidden">
              <img src="https://avatar.iran.liara.run/public" alt="Team Member" class="w-full h-64 object-cover"/>
              <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity flex items-end justify-center pb-6">
                <div class="flex space-x-4">
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                  </a>
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  </a>
                </div>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-xl font-semibold text-white mb-2">John Anderson</h3>
              <p class="text-neutral-400">Chief Technology Officer</p>
            </div>
          </div>
        </div>

        <!-- Team Member 2 -->
        <div class="group animate__animated animate__fadeInUp animate__delay-1s">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden transition-transform duration-300 transform hover:-translate-y-2">
            <div class="relative overflow-hidden">
              <img src="https://avatar.iran.liara.run/public" alt="Team Member" class="w-full h-64 object-cover"/>
              <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity flex items-end justify-center pb-6">
                <div class="flex space-x-4">
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                  </a>
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  </a>
                </div>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-xl font-semibold text-white mb-2">Sarah Wilson</h3>
              <p class="text-neutral-400">Lead Engineer</p>
            </div>
          </div>
        </div>

        <!-- Team Member 3 -->
        <div class="group animate__animated animate__fadeInUp animate__delay-2s">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden transition-transform duration-300 transform hover:-translate-y-2">
            <div class="relative overflow-hidden">
              <img src="https://avatar.iran.liara.run/public" alt="Team Member" class="w-full h-64 object-cover"/>
              <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity flex items-end justify-center pb-6">
                <div class="flex space-x-4">
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                  </a>
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  </a>
                </div>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-xl font-semibold text-white mb-2">Michael Chen</h3>
              <p class="text-neutral-400">System Architect</p>
            </div>
          </div>
        </div>

        <!-- Team Member 4 -->
        <div class="group animate__animated animate__fadeInUp animate__delay-3s">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl overflow-hidden transition-transform duration-300 transform hover:-translate-y-2">
            <div class="relative overflow-hidden">
              <img src="https://avatar.iran.liara.run/public" alt="Team Member" class="w-full h-64 object-cover"/>
              <div class="absolute inset-0 bg-gradient-to-t from-neutral-900 to-transparent opacity-0 group-hover:opacity-90 transition-opacity flex items-end justify-center pb-6">
                <div class="flex space-x-4">
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                  </a>
                  <a href="#" class="text-white hover:text-indigo-400 transition-colors">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  </a>
                </div>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-xl font-semibold text-white mb-2">Emma Thompson</h3>
              <p class="text-neutral-400">Project Manager</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate__animated');
          entry.target.style.visibility = 'visible';
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      element.style.visibility = 'hidden';
      observer.observe(element);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <section id="contact" class="py-20 bg-neutral-800 relative overflow-hidden">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>
    <div class="absolute top-0 right-0 w-96 h-96 bg-indigo-600/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-purple-600/10 rounded-full blur-3xl"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold text-white mb-4 animate__animated animate__fadeInUp">Get In Touch</h2>
        <p class="text-neutral-300 max-w-2xl mx-auto animate__animated animate__fadeInUp animate__delay-1s">
          Have questions about our water management solutions? We'd love to hear from you.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Contact Information -->
        <div class="space-y-8 animate__animated animate__fadeInLeft">
          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300">
            <div class="flex items-center space-x-4">
              <div class="flex-shrink-0">
                <div class="p-4 bg-indigo-600/20 rounded-lg">
                  <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                  </svg>
                </div>
              </div>
              <div>
                <h3 class="text-white font-semibold mb-1">Phone</h3>
                <p class="text-neutral-300">+1 (555) 123-4567</p>
              </div>
            </div>
          </div>

          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300">
            <div class="flex items-center space-x-4">
              <div class="flex-shrink-0">
                <div class="p-4 bg-indigo-600/20 rounded-lg">
                  <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                  </svg>
                </div>
              </div>
              <div>
                <h3 class="text-white font-semibold mb-1">Email</h3>
                <p class="text-neutral-300">info@example.com</p>
              </div>
            </div>
          </div>

          <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-6 hover:bg-white/10 transition-all duration-300">
            <div class="flex items-center space-x-4">
              <div class="flex-shrink-0">
                <div class="p-4 bg-indigo-600/20 rounded-lg">
                  <svg class="w-6 h-6 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                </div>
              </div>
              <div>
                <h3 class="text-white font-semibold mb-1">Location</h3>
                <p class="text-neutral-300">123 Business Street, Tech City, 12345</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="backdrop-blur-lg bg-white/5 border border-neutral-700 rounded-xl p-8 animate__animated animate__fadeInRight">
          <form id="contactForm" class="space-y-6">
            <div>
              <label for="name" class="block text-white mb-2">Name</label>
              <input type="text" id="name" name="name" required
                class="w-full px-4 py-3 rounded-lg bg-white/5 border border-neutral-600 text-white placeholder-neutral-400 focus:outline-none focus:border-indigo-500 transition-colors"
                placeholder="Your Name">
            </div>

            <div>
              <label for="email" class="block text-white mb-2">Email</label>
              <input type="email" id="email" name="email" required
                class="w-full px-4 py-3 rounded-lg bg-white/5 border border-neutral-600 text-white placeholder-neutral-400 focus:outline-none focus:border-indigo-500 transition-colors"
                placeholder="your@email.com">
            </div>

            <div>
              <label for="message" class="block text-white mb-2">Message</label>
              <textarea id="message" name="message" rows="4" required
                class="w-full px-4 py-3 rounded-lg bg-white/5 border border-neutral-600 text-white placeholder-neutral-400 focus:outline-none focus:border-indigo-500 transition-colors"
                placeholder="Your message..."></textarea>
            </div>

            <button type="submit"
              class="w-full py-3 px-6 rounded-lg bg-indigo-600 text-white font-semibold hover:bg-indigo-700 transition-colors transform hover:scale-[1.02] duration-300">
              Send Message
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <script>
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.visibility = 'visible';
          entry.target.classList.add('animate__animated');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      element.style.visibility = 'hidden';
      observer.observe(element);
    });

    // Form Submission
    document.getElementById('contactForm').addEventListener('submit', function(e) {
      e.preventDefault();
      
      // Add form submission animation
      const button = this.querySelector('button[type="submit"]');
      button.innerHTML = 'Sending...';
      button.disabled = true;
      
      // Simulate form submission
      setTimeout(() => {
        button.innerHTML = 'Message Sent!';
        button.classList.add('bg-green-600');
        
        // Reset form after delay
        setTimeout(() => {
          this.reset();
          button.innerHTML = 'Send Message';
          button.classList.remove('bg-green-600');
          button.disabled = false;
        }, 2000);
      }, 1500);
    });
  </script>
</div>
</htmlCode><htmlCode>
<div id="root">
  <footer id="footer" class="bg-neutral-900 relative">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/10 to-purple-600/10"></div>

    <!-- Main Footer Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 pt-16 pb-8 border-b border-neutral-800">
        <!-- Company Info -->
        <div class="animate__animated animate__fadeInUp">
          <h3 class="text-2xl font-bold text-white mb-4">MRS</h3>
          <p class="text-neutral-400 mb-6">Advanced water management solutions for sustainable future.</p>
          <div class="flex space-x-4">
            <a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
              </svg>
            </a>
            <a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm3 8h-1.35c-.538 0-.65.221-.65.778v1.222h2l-.209 2h-1.791v7h-3v-7h-2v-2h2v-2.308c0-1.769.931-2.692 3.029-2.692h1.971v3z"/>
              </svg>
            </a>
            <a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">
              <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 16h-2v-6h2v6zm-1-6.891c-.607 0-1.1-.496-1.1-1.109 0-.612.492-1.109 1.1-1.109s1.1.497 1.1 1.109c0 .613-.493 1.109-1.1 1.109zm8 6.891h-1.998v-2.861c0-1.881-2.002-1.722-2.002 0v2.861h-2v-6h2v1.093c.872-1.616 4-1.736 4 1.548v3.359z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="animate__animated animate__fadeInUp animate__delay-1s">
          <h4 class="text-lg font-semibold text-white mb-4">Quick Links</h4>
          <ul class="space-y-3">
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">About Us</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Services</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Portfolio</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Contact</a></li>
          </ul>
        </div>

        <!-- Services -->
        <div class="animate__animated animate__fadeInUp animate__delay-2s">
          <h4 class="text-lg font-semibold text-white mb-4">Our Services</h4>
          <ul class="space-y-3">
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Water Management</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Quality Control</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Distribution Systems</a></li>
            <li><a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Monitoring Solutions</a></li>
          </ul>
        </div>

        <!-- Newsletter -->
        <div class="animate__animated animate__fadeInUp animate__delay-3s">
          <h4 class="text-lg font-semibold text-white mb-4">Newsletter</h4>
          <p class="text-neutral-400 mb-4">Subscribe to our newsletter for updates.</p>
          <form class="space-y-4">
            <div class="relative">
              <input type="email" placeholder="Enter your email" 
                class="w-full px-4 py-3 rounded-lg bg-white/5 border border-neutral-700 text-white placeholder-neutral-500 focus:outline-none focus:border-indigo-500 transition-colors">
            </div>
            <button type="submit" 
              class="w-full py-3 px-6 rounded-lg bg-indigo-600 text-white font-semibold hover:bg-indigo-700 transition-colors transform hover:scale-[1.02] duration-300">
              Subscribe
            </button>
          </form>
        </div>
      </div>

      <!-- Bottom Footer -->
      <div class="py-6 text-center md:flex md:justify-between md:text-left">
        <p class="text-neutral-400 mb-4 md:mb-0">
          © 2024 MRS. All rights reserved.
        </p>
        <div class="space-x-6">
          <a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Privacy Policy</a>
          <a href="#" class="text-neutral-400 hover:text-indigo-500 transition-colors">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.visibility = 'visible';
          entry.target.classList.add('animate__animated');
        }
      });
    }, {
      threshold: 0.1
    });

    document.querySelectorAll('.animate__animated').forEach((element) => {
      element.style.visibility = 'hidden';
      observer.observe(element);
    });
  </script>
</div>
</htmlCode>
