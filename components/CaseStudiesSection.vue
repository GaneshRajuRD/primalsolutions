<template>
    <div class="container py-5" v-if="caseStudies.length > 0">
        <div class="row">
            <div class="col-sm-12 col-lg-5">
                <h4 class="gearIcon fw-bold">OUR CASESTUDIES</h4>
                <h2 class="fw-light">Insights from our <span class="fw-bold"> Projects</span></h2>
            </div>
            <div class="col-sm-0 col-lg-1 px-0"></div>
            <div class="col-sm-12 col-lg-6">
                <p>
                    We help manufacturing companies, especially in the automotive sector, enhance operational efficiency, develop effective strategies, and deliver measurable results that directly improve the bottom line through real-time, proven solutions.
                </p>
                <NuxtLink :to="viewMoreUrl" class="blueBtn">View More</NuxtLink>
            </div>
        </div>

        <div ref="sliderEl" class="splide py-sm-4 py-2 caseStudy-slider" v-if="caseStudies.length > 0">
            <div class="splide__track py-4">
                <ul class="splide__list">
                    <li class="splide__slide" v-for="caseStudy in caseStudies" :key="caseStudy.url || caseStudy.title">
                        <CaseStudyCard :caseStudy="caseStudy" />
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, ref, nextTick } from "vue";

const props = defineProps({
    caseStudies: {
        type: Array,
        required: true,
    },
    title: {
        type: String,
        default: 'latest Projects',
    },
    description: {
        type: String,
        default: 'Real examples of how we’ve helped automotive, FMCG, electronics, and industrial clients improve productivity, strengthen quality, and scale performance.',
    },
    viewMoreUrl: {
        type: String,
        default: '/resources#CaseStudies',
    },
});

const sliderEl = ref(null);
let splideInstance = null;

const splideOptions = {
    drag: "free",
    focus: 0,
    omitEnd: true,
    snap: true,
    arrows: true,
    indicators: true,
    breakpoints: {
        2600: { perPage: 2 },
        1440: { perPage: 2 },
        1024: { perPage: 2 },
        768: { perPage: 2 },
        576: { perPage: 1 },
    },
};

const mountSplide = () => {
    if (!sliderEl.value || splideInstance) return;
    const SplideCtor = window.Splide;
    if (!SplideCtor) {
        setTimeout(mountSplide, 100);
        return;
    }
    splideInstance = new SplideCtor(sliderEl.value, splideOptions);
    splideInstance.mount();
};

onMounted(async () => {
    await nextTick();
    mountSplide();
});

onBeforeUnmount(() => {
    if (splideInstance) {
        try { splideInstance.destroy(); } catch (e) { /* noop */ }
        splideInstance = null;
    }
});
</script>
