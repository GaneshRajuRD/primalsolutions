<template>
    <div ref="textSlideRef" :class="['text-slide', { 'text-slide-visible': isVisible }]" :style="slideStyle">
        <slot></slot>
    </div>
</template>
<script setup>
import { ref, onMounted, computed } from 'vue'

const props = defineProps({
    delay: {
        type: Number,
        default: 0
    }
})

const textSlideRef = ref(null)
const isVisible = ref(false)
const hasAnimated = ref(false)

const slideStyle = computed(() => ({
    transitionDelay: props.delay ? `${props.delay}ms` : '0ms'
}))

onMounted(() => {
    const observer = new IntersectionObserver(
        ([entry]) => {
            if (entry.isIntersecting && !hasAnimated.value) {
                isVisible.value = true
                hasAnimated.value = true
                observer.disconnect()
            }
        },
        {
            threshold: 0.7 // Trigger when 70% of the element is visible
        }
    )

    if (textSlideRef.value) {
        observer.observe(textSlideRef.value)
    }
})
</script>
<style scoped>
.text-slide {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s ease-out;
    will-change: transform, opacity;
}

.text-slide-visible {
    opacity: 1;
    transform: translateY(0);
}
</style>