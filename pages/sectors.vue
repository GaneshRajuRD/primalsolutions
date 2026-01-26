<template>
    <div class="body">

        <Header />

        <div class="aboutUsBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-bold">Sectors</h1>
                    <p>
                        Explore exciting opportunities and grow your career in property management with us
                    </p>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="whyUsCard">
                <div class="row">
                    <div class="col-lg-6">
                        <img src="/assets/image/sectorImg.webp" class="w-100 mb-4 mb-lg-0 img-fluid" alt="">
                    </div>
                    <div class="col-lg-6">
                        <div class="content ps-lg-3">
                            <h2 class="bigFont text-white">Why Choose Primal Solutions</h2>
                            <p>
                                 We turn strategic vision into measurable results through hands-on, execution-focused consulting. Combining deep industry expertise with performance-driven frameworks, we help organizations optimize operations, enter markets successfully, and build lasting competitive advantage—aligning strategy, operations, and capability development for sustainable growth.
                            </p>
                            <a href="/contact-us" class="arrowBtn">
                                Contact Us <span class="material-symbols-outlined">arrow_right_alt</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5">
            <h4 class="text-center mb-4">Sectors We Transform</h4>
            <div class="row g-4">
                <div class="col-sm-12 col-md-6 col-lg-4" v-for="sector in sectors">
                    <SectorCard :sector="sector" />
                </div>
            </div>
        </div>
        

        <ContactFormBg />
        <ContactForm />

        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">LATEST BLOG</h4>
                    <h2 class="fw-light">Insights from our <span class="fw-bold">latest blogs</span></h2>
                </div>
                <div class="col-sm-0 col-lg-1 px-0"></div>
                <div class="col-sm-12 col-lg-6">
                    <p class="mt-4 pt-2">
                        Stay updated with practical strategies, industry trends, and proven improvement methods tailored for modern manufacturing.
                    </p>
                    <NuxtLink to="/resources#Blogs" class="blueBtn">View More</NuxtLink>
                </div>
            </div>

            <div class="splide py-sm-4 py-2 blog-slider">
                <div class="splide__track py-4">
                    <ul class="splide__list">
                        <li class="splide__slide" v-for="blog in blogs">
                            <BlogCard :blog="blog" />
                        </li>
                    </ul>
                </div>
            </div>
                
        </div>
        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">OUR CASESTUDIES</h4>
                    <h2 class="fw-light">Insights from our <span class="fw-bold">latest Projects</span></h2>
                </div>
                <div class="col-sm-0 col-lg-1 px-0"></div>
                <div class="col-sm-12 col-lg-6">
                    <p class="mt-4 pt-2">
                        Real examples of how we’ve helped automotive, FMCG, electronics, and industrial clients improve productivity, strengthen quality, and scale performance.
                    </p>
                    <NuxtLink to="/resources#CaseStudies" class="blueBtn">View More</NuxtLink>
                </div>
            </div>

            <div class="splide py-sm-4 py-2 caseStudy-slider">
                <div class="splide__track py-4">
                    <ul class="splide__list">
                        <li class="splide__slide" v-for="caseStudy in caseStudies">
                            <CaseStudyCard :caseStudy="caseStudy" />
                        </li>
                    </ul>
                </div>
            </div>
                
        </div>

        <Footer />
        
    </div>
</template>
<script setup>
import { onMounted } from "vue";

import { blogs } from '~/data/blogs.js';
import { caseStudies } from '~/data/caseStudies.js';
const sectors = ref([
    {
        title: 'Automotive Manufacturing',
        description: 'We help automotive plants improve line efficiency, reduce defects, and build scalable production systems across complex, fast-moving operations.',
        image: '/assets/image/Automotive-Manufacturing.webp',
        services: [
            'Line balancing and single-piece flow',
            'Zero-defect culture deployment',
            'Plant layout optimization and re-layout',
            'Supply-chain improvement for OEM/Tier-I',
            'Productivity improvement and lean programs',
            'KPI deployment and operational monitoring',
        ],
    },
    {
        title: 'Agricultural & Farm Equipment',
        description: 'We help farm-equipment manufacturers improve assembly accuracy, reduce breakdown-related rework, and build reliable production systems that support seasonal output.',
        image: '/assets/image/Agricultural-Farm-Equipment.webp',
        services: [
            'Line balancing for tractor and farm units',
            'Zero-defect checks for mechanical builds',
            'Layout upgrades for smooth material flow',
            'Supplier and component quality programs',
            'Lean adoption for varied product models',
            'KPI visibility and daily performance review',
        ],
    },
    {
        title: 'Elevators & Construction Equipment',
        description: 'We help elevator and construction-equipment plants enhance build precision, reduce installation defects, and create scalable assembly systems for heavy-duty products.',
        image: '/assets/image/Elevators-Construction-Equipment.webp',
        services: [
            'Standardized processes for major assemblies',
            'Quality controls for safety-critical parts',
            'Layout optimization for structural builds',
            'Supply-chain accuracy and BOM alignment',
            'Lean flow for fabrication and assembly lines',
            'KPI tracking for production performance',
        ],
    },
    {
        title: 'Off-Road & Earthmoving Industry',
        description: 'We help earthmoving-equipment makers strengthen durability, stabilize heavy-component flow, and improve reliability across demanding production operations.',
        image: '/assets/image/Off-Road-Earthmoving-Industry.webp',
        services: [
            'Optimization of chassis and frame lines',
            'Quality systems for rugged equipment use',
            'Heavy-part logistics and material flow',
            'Supplier improvement for castings/forgings',
            'Lean techniques for slow-cycle assemblies',
            'KPI monitoring for build consistency',
        ],
    },
    {
        title: 'FMCG Manufacturing',
        description: 'We help FMCG plants increase throughput, reduce changeover losses, and build fast, reliable production environments suited for high-speed packaging lines.',
        image: '/assets/image/FMCG-Manufacturing.webp',
        services: [
            'Line balancing for fast-moving packs',
            'Quality and hygiene compliance setup',
            'Layout redesign for continuous flow',
            'Warehouse and dispatch optimization',
            'Lean and TPM-based productivity boosts',
            'Real-time KPI and downtime tracking',
        ],
    },
    {
        title: 'Electronics Production',
        description: 'We help electronics manufacturers improve yield, reduce defects, and create stable, scalable processes across SMT lines, assembly cells, and testing stations.',
        image: '/assets/image/Electronics-Production.webp',
        services: [
            'Optimization of SMT and assembly flow',
            'Yield improvement using defect analysis',
            'ESD and quality-system implementation',
            'Supplier quality for key components',
            'Lean flow for high-mix production units',
            'KPI dashboards for production control',
        ],
    },
]);

onMounted(() => {

    const splide2 = new Splide(".blog-slider", {
        drag: "free",
        focus: 0,
        omitEnd: true,
        snap: true,
        arrows: true,
        indicators: true,
        breakpoints: {
            2600: {
                perPage: 2,
            },
            1440: {
                perPage: 2,
            },
            1024: {
                perPage: 2,
            },
            768: {
                perPage: 2,
            },
            576: {
                perPage: 1,
            },
        },
    });
    splide2.mount();
    const splide3 = new Splide(".caseStudy-slider", {
        drag: "free",
        focus: 0,
        omitEnd: true,
        snap: true,
        arrows: true,
        indicators: true,
        breakpoints: {
            2600: {
                perPage: 2,
            },
            1440: {
                perPage: 2,
            },
            1024: {
                perPage: 2,
            },
            768: {
                perPage: 2,
            },
            576: {
                perPage: 1,
            },
        },
    });
    splide3.mount();

});

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.aboutUsBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/sectorsBnr.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
.aboutUsBnr h1{
    color: #fff;
}

.aboutUsBnr .content {
    height: 90vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}

.aboutUsBnr .content h1 {
    font-size: 60px;
}


.whyUsCard{
    background-color: #282828;
    padding: 1.5em;
    margin: 4em 0;
    color: #fff;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    .aboutUsBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .aboutUsBnr .content h1 {
        font-size: 44px;
    }
}
@media only screen and (max-width:830px) {
    .aboutUsBnr .content h1 {
        font-size: 40px;
    }
}
@media only screen and (max-width:578px) {
    
}
</style>