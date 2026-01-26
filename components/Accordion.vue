<template>
    <div class="accordionSec">
        <div class="accordion testAccordion">
            <div v-for="(accordion, index) in localaccordions" :key="index" class="accordion__item" :class="{ 'accordion__item--active': accordion.active }">
                <button class="accordion__btn" @click="toggleAccordion(index)">
                    <p class="accordion__caption mb-0"><span class="caption-index">{{ index + 1 }}.</span> {{ accordion?.question }}</p>
                    <span class="accordion__icon">
                        <span class="material-symbols-outlined">arrow_forward_ios</span>
                    </span>
                </button>
                <div class="accordion__content">
                    <div class="px-2 px-sm-3 pb-sm-3">
                        <p class="grey-text mb-1">
                            {{ accordion?.answer }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
    accordions: {
        type: Array,
        required: true
    }
});

// Create a local reactive copy of the accordions
const localaccordions = ref([]);

// Initialize local accordions when component mounts
const initializeaccordions = (accordions) => {
    return Array.isArray(accordions) ? accordions.map((accordion, index) => ({
        ...accordion,
        active: index === 0
    })) : [];
};

// Initialize on mount
localaccordions.value = initializeaccordions(props.accordions);

// Watch for changes in props.accordions and update local copy
watch(() => props.accordions, (newaccordions) => {
    localaccordions.value = initializeaccordions(newaccordions);
}, { deep: true });

const toggleAccordion = (index) => {
    localaccordions.value.forEach((accordion, i) => {
        accordion.active = (i === index && !accordion.active);
    });
};

</script>
<style scoped>
.accordionSec .accordion {
    border-radius: 1rem;
    position: relative;
    z-index: 2;
}

.accordionSec .accordion .accordion__caption {
    color: #111F61;
}

.accordionSec .accordion__caption .caption-index {
    font-weight: 700;
    margin-right: 0.2rem;
}

.accordionSec .accordion .accordion__icon {
    border-radius: 50%;
}

.accordionSec .accordion__item--active .accordion__icon{
    transition: 0.5s;
}
.accordionSec .accordion .accordion__icon span{
    color: #222222;
    font-weight: 300;
    font-size: 16px;
}
.accordionSec .accordion__heading {
    margin-bottom: 2rem;
    padding: 0 1.4rem;
}

.accordionSec .accordion__item {
    margin-bottom: 25px;
    background-color: #fff;  
    border: 1px solid #EBEBEB;
    border-radius: 6px;
}
.accordionSec .accordion__item--active .accordion__caption,
.accordionSec .accordion__item--active .accordion__content{
    transition: 0.6s;
}
.accordionSec .accordion__item--active{
    box-shadow: 12px 12px 50px rgb(0, 0, 0, 0.08);
    background-color: #111F61;
}
.accordionSec .accordion__item--active p,
.accordionSec .accordion__item--active .accordion__caption,
.accordionSec .accordion__item--active span{
    color: #fff !important;
}

.accordionSec .accordion__btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 1rem 1.2rem;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1.2rem;
    text-align: left;
    cursor: pointer;
    transition: 0.1s;
    border-radius: 6px;
}

.accordionSec .fa-lightbulb {
    padding-right: 1rem;
}

.accordionSec .accordion__icon {
    transition: transform 0.3s ease-in-out;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transform: rotate(0deg);
}

.accordionSec .accordion__item--active .accordion__icon {
    transform: rotate(90deg);
    color: #fff;
}

.accordionSec .accordion__content {
    font-weight: 300;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transform: translateX(16px);
    transition: max-height 0.5s ease, opacity 0.5s, transform 0.5s;
}

.accordionSec .accordion__item--active .accordion__content {
    opacity: 1;
    transform: translateX(0px);
    max-height: 100vh;
}

.accordionSec .testAccordion .accordion__caption {
    font-weight: 500;
}
@media only screen and (max-width: 578px) {
    .accordion__content p{
        font-size: 14px;
    }
}
</style>
