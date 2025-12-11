<template>
  <header :class="{ 'header-hidden': !isVisible }">
    <!-- Top Bar -->

    <!-- Main Header -->
    <div class="container">
        <div class="main-header">
        <div class="d-flex justify-content-between align-items-center">
          <div class="logo">
            <NuxtLink to="/">
              <img src="/assets/image/primalLogo.png" alt="PRIMAL" />
            </NuxtLink>
          </div>

          <button class="mobile-menu-toggle" @click="toggleMobileMenu" :class="{ 'is-active': isMobileMenuOpen }">
            <span></span>
            <span></span>
            <span></span>
          </button>

          <nav class="main-nav" :class="{ 'is-open': isMobileMenuOpen }">
            <div class="nav-content">
              <ul class="menuList">
                <li :class="{ active: isHomeActive }">
                  <NuxtLink to="/">Home</NuxtLink>
                </li>
                <li :class="{ active: isAboutActive }">
                  <NuxtLink to="/about-us">About us</NuxtLink>
                </li>
                <li class="dropdown" :class="{ 'is-open': isDropdownOpen, active: isServiceActive }">
                  <a href="#" @click.prevent="toggleDropdown" class="dropdown-toggle">
                    Services
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M6 9l6 6 6-6" />
                    </svg>
                  </a>
                  <ul class="dropdown-menu">
                    <li><NuxtLink to="/services/business-strategy">Business Strategy</NuxtLink></li>
                    <li><NuxtLink to="/services/business-transformation">Business Transformation</NuxtLink></li>
                    <li><NuxtLink to="/services/skill-development-programs">Skill Development Programs</NuxtLink></li>
                    <li><NuxtLink to="/services/operations-supply-chain-excellence">Operations & Supply Chain Excellence</NuxtLink></li>
                    <li><NuxtLink to="/services/talent-hiring-management">Talent Hiring & Management</NuxtLink></li>
                    <li><NuxtLink to="/services/market-research">Market Research</NuxtLink></li>
                  </ul>
                </li>
                <li :class="{ active: isSectorsActive }">
                  <NuxtLink to="/sectors">Sectors</NuxtLink>
                </li>
                <li :class="{ active: isResourcesActive }">
                  <NuxtLink to="/resources">Resources</NuxtLink>
                </li>
                <li :class="{ active: isCareersActive }">
                  <NuxtLink to="/careers">Careers</NuxtLink>
                </li>
              </ul>
              <NuxtLink to="/contact-us" class="headerBtn">Contact us</NuxtLink>
            </div>
          </nav>
        </div>
      </div>
    </div>
</header>
<button @click="scrollToTop" class="move-to-top-btn" v-show="isButtonVisible">
  <span data-v-a7322cec="" class="material-symbols-outlined">arrow_upward</span>
</button>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const isMobileMenuOpen = ref(false);
const isDropdownOpen = ref(false);

const isVisible = ref(true);
const isButtonVisible = ref(false);
let lastScrollY = 0;

const handleScroll = () => {
    const currentScrollY = window.scrollY;
    // Always show header when menu is open or near top
    if (isMobileMenuOpen.value || currentScrollY < 200) {
        isVisible.value = true;
    } else {
        isVisible.value = currentScrollY < lastScrollY;
    }
    // Show button only when scrolled below 150vh
    isButtonVisible.value = currentScrollY > window.innerHeight * 0.4;
    lastScrollY = currentScrollY;
};

const toggleMobileMenu = () => {
    isMobileMenuOpen.value = !isMobileMenuOpen.value;
    if (!isMobileMenuOpen.value) {
        isDropdownOpen.value = false;
    }
};

const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value;
};

// Check if any dropdown child route is active
const isServiceActive = computed(() => {
    const currentPath = route.path;
    const serviceRoutes = ["/services/"];
    return serviceRoutes.some((path) => currentPath.startsWith(path));
});

// Active states for menu items
const isHomeActive = computed(() => route.path === '/');
const isAboutActive = computed(() => route.path === '/about-us');
const isSectorsActive = computed(() => route.path === '/sectors');
const isResourcesActive = computed(() => route.path === '/resources');
const isCareersActive = computed(() => route.path === '/careers');
const isContactActive = computed(() => route.path === '/contact-us');

// Close dropdown when route changes
watch(
    () => route.path,
    () => {
        isDropdownOpen.value = false;
    }
);

const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
};

onMounted(() => {
    window.addEventListener("scroll", handleScroll);
});
onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0');

header {
    position: fixed;
    top: 0;
    width: 100%;
    top: 30px;
    z-index: 999;
    transform: translateY(0);
    transition: transform 0.3s ease;
}

header.header-hidden {
    transform: translateY(-140%);
}

.contactSec {
    display: flex;
    align-items: center;
    gap: 15px;
}

.contactSec a {
    font-family: "Merriweather Sans", sans-serif;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.contactSec a span {
    font-size: 16px;
    color: #fff;
}

.top-bar {
    background: #f9c12e;
    padding: 8px 0;
}

.top-links {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
}

.top-links a {
    color: white;
    text-decoration: none;
    font-size: 14px;
    transition: opacity 0.3s;
}

.top-links a:hover {
    opacity: 0.8;
}

/* Main Header */
.main-header {
  background: #00000040;
    border: 2px solid #fff;
    border-radius: 80px;
    padding: 10px 15px 10px 25px;
    backdrop-filter: blur(15px);
}

.logo img {
    height: 55px;
    width: auto;
}

/* Mobile Menu Toggle */
.mobile-menu-toggle {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 20px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 10;
    display: none;
}

.mobile-menu-toggle span {
    width: 100%;
    height: 2px;
    background-color: #fff;
    transition: all 0.3s ease;
}
.mobile-menu-toggle.is-active span{
  background-color: #444;
}
.mobile-menu-toggle.is-active span:first-child {
    transform: translateY(9px) rotate(45deg);
}

.mobile-menu-toggle.is-active span:nth-child(2) {
    opacity: 0;
}

.mobile-menu-toggle.is-active span:last-child {
    transform: translateY(-9px) rotate(-45deg);
}

/* Main Navigation */
.main-nav .menuList {
    display: inline-flex;
    flex-wrap: wrap;
    flex-direction: row;
    list-style: none;
    gap: 32px;
    margin: 0;
    padding: 0;
}

.main-nav a {
    text-decoration: none;
    color: #fff;
    font-size: 16px;
    transition: color 0.3s;
    display: flex;
    align-items: center;
    gap: 4px;
}

.main-nav a:hover {
    color: #f9c12e !important;
}

.menuList li.active a {
    color: #f9c12e;
    font-weight: bold;
}

/* Dropdown */
.dropdown {
    position: relative;
}

.dropdown-menu {
    position: absolute;
    top: 30px;
    left: 0;
    background: white;
    min-width: 200px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(10px);
    transition: all 0.3s;
    z-index: 1000;
    padding: 0;
    list-style: none;
    display: block;
}

.dropdown:hover .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
    display: block;
}

.dropdown-menu li {
    padding: 0;
}

.dropdown-menu a {
    color: #000 !important;
    font-weight: normal !important;
    padding: 8px 16px;
    display: block;
    white-space: nowrap;
}

.dropdown-menu a:hover {
    background: #f5f5f5;
}

.headerBtn {
    background-color: #fff;
    color: #000 !important;
    text-decoration: none;
    padding: 12px 30px;
    border-radius: 30px;
}

.dropdown-toggle::after {
    display: none;
}

.nav-content {
    display: inline-flex;
    align-items: center;
    height: 100%;
    gap: 15px;
}

/* Mobile Responsive */
@media (max-width: 820px) {
  .main-nav a {
      color: #000;
  }
  .headerBtn{
    color: #fff !important;
  }
    .menuList {
        flex-direction: column !important;
    }

    .container {
        padding: 0 15px;
    }

    .top-links {
        justify-content: center;
        flex-wrap: wrap;
        gap: 16px;
    }

    .mobile-menu-toggle {
        display: flex !important;
        margin-left: auto;
        right: 20px;
        z-index: 10;
        margin-right: 5px;
    }

    .nav-content {
        display: inline-flex;
        align-items: flex-start;
        flex-direction: column;
        height: 100%;
        gap: 20px;
        margin-left: 10px;
    }

    .main-nav {
        position: fixed;
        top: 0;
        left: -10%;
        width: 100%;
        border-radius: 30px;
        background: white;
        padding: 60px 20px 20px;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
        z-index: 5;
        overflow-y: auto;
    }

    .main-nav.is-open {
        transform: translateX(10%);
    }

    .main-nav ul {
        flex-direction: column;
        gap: 20px;
    }

    .logo img {
        height: 55px;
    }
    .headerBtn {
        background-color: #111F61;
        color: #000;
        text-decoration: none;
        padding: 15px 30px;
        border-radius: 30px;
    }
}

@media (max-width: 480px) {
    .top-links {
        font-size: 12px;
        gap: 12px;
    }

    .logo img {
        height: 50px;
    }
}

@media (max-width: 578px) {
    .secondaryContact {
        display: none !important;
    }
}

.move-to-top-btn {
    position: fixed;
    bottom: 10px;
    left: 20px;
    background: #111F61;
    border: none;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s ease;
    z-index: 1000;
}

.move-to-top-btn:hover {
    background: #0e1a53;
    box-shadow: 0px 2px 8px rgb(0, 0, 0, 0.6);
    transition: 0.4s;
}

.move-to-top-btn span {
    font-size: 24px;
    color: #fff;
}
</style>
