<template>
    <div class="accordionSec">
        <div class="accordion testAccordion">
            <div v-for="(faq, index) in localFaqs" :key="index" class="accordion__item" :class="{ 'accordion__item--active': faq.active }">
                <button class="accordion__btn" @click="toggleAccordion(index)">
                    <p class="accordion__caption mb-0">{{ faq?.question }}</p>
                    <span class="accordion__icon">
                        <span class="material-symbols-outlined">arrow_forward_ios</span>
                    </span>
                </button>
                <div class="accordion__content">
                    <div class="px-2 px-sm-3 py-sm-3">
                        <p class="grey-text mb-1">
                            {{ faq?.answer }}
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
    faqs: {
        type: Array,
        required: true
    }
});

// Create a local reactive copy of the faqs
const localFaqs = ref([]);

// Initialize local faqs when component mounts
const initializeFaqs = (faqs) => {
    return Array.isArray(faqs) ? faqs.map((faq, index) => ({
        ...faq,
        active: index === 0
    })) : [];
};

// Initialize on mount
localFaqs.value = initializeFaqs(props.faqs);

// Watch for changes in props.faqs and update local copy
watch(() => props.faqs, (newFaqs) => {
    localFaqs.value = initializeFaqs(newFaqs);
}, { deep: true });

const toggleAccordion = (index) => {
    localFaqs.value.forEach((faq, i) => {
        faq.active = (i === index && !faq.active);
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
    color: #222222;
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
.accordionSec .accordion__item--active{
    background-color: #111F61;
}
.accordionSec .accordion__item--active .accordion__caption,
.accordionSec .accordion__item--active .accordion__content{
    color: #fff;
    transition: 0.6s;
}
.accordionSec .accordion .accordion__item--active  .accordion__icon span {
    color: #fff;
}
.accordionSec .accordion .accordion__item--active  .accordion__btn {
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
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
