<template>
    <div class="loader-overlay" v-if="isVisible">
        <div class="loader-container">
            <div class="logo-container">
                <img src="/assets/image/primalLogo.png" alt="Primal Solutions Logo" class="loader-logo" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from "vue";

// Define props
const props = defineProps({
    time: {
        type: Number,
        default: null,
        validator: (value) => value === null || value > 0
    }
});

const isVisible = ref(true);

const hideLoader = () => {
    isVisible.value = false;
};

defineExpose({
    hideLoader
});

onMounted(async () => {
    // Wait for next tick to ensure DOM is ready
    await nextTick();
    
    if (typeof window !== 'undefined') {
        // If time prop is provided, hide loader after specified time
        if (props.time !== null) {
            setTimeout(() => {
                hideLoader();
            }, props.time);
            return;
        }
        
        // Hide loader when page is ready or after timeout (whichever comes first)
        const hideLoaderSafely = () => {
            if (isVisible.value) {
                hideLoader();
            }
        };
        
        // Use window load event as primary trigger
        window.addEventListener('load', hideLoaderSafely, { once: true });
        
        // Fallback: hide loader after 3 seconds max
        setTimeout(hideLoaderSafely, 3000);
    }
});

</script>

<style scoped>
.loader-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #9196b1, rgb(255, 255, 255));
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    transition: opacity 0.5s ease-in-out;
}

.loader-container {
    text-align: center;
    position: relative;
}

.logo-container {
    position: relative;
    display: inline-block;
    margin-bottom: 30px;
}

.loader-logo {
    width: 250px;
    height: auto;
    position: relative;
    z-index: 2;
    animation: breathe 2s ease-in-out infinite;
}

@keyframes breathe {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
    100% {
        opacity: 1;
    }
}

@keyframes logoFloat {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

@keyframes textPulse {
    0%, 100% {
        opacity: 0.7;
    }
    50% {
        opacity: 1;
    }
}

@keyframes fadeOut {
    to {
        opacity: 0;
        visibility: hidden;
    }
}

@media only screen and (max-width: 780px) {
    .loader-logo {
        width: 150px;
    }
    
    .pulse-ring {
        width: 130px;
        height: 130px;
    }
    
    .loading-text {
        font-size: 16px;
    }
}

@media only screen and (max-width: 578px) {
    .loader-logo {
        width: 150px;
    }
    
    .pulse-ring {
        width: 110px;
        height: 110px;
    }
    
    .loading-text {
        font-size: 14px;
    }
}
</style>
