<template>
  <div ref="element" :class="{ 'slide-from-bottom': true, 'visible': isVisible }" :style="animationStyle">
    <slot></slot>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'

const props = defineProps({
  delay: {
    type: Number,
    default: 0
  }
})

const element = ref(null)
const isVisible = ref(false)
let observer = null

const animationStyle = computed(() => ({
  transitionDelay: `${props.delay * 0.2}s`
}))

onMounted(() => {
  observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      isVisible.value = true
      observer.disconnect()
    }
  }, {
    threshold: 0.1
  })

  if (element.value) {
    observer.observe(element.value)
  }
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>

<style scoped>
.slide-from-bottom {
  transform: translateY(50px);
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
}

.slide-from-bottom.visible {
  transform: translateY(0);
}
</style>
