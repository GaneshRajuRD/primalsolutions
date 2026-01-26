<template>
    <div class="body">

        <Header />

        <div class="homeBnr">
            <div class="container">
                <div class="row">
                    <div class="col-sm-9 col-lg-6">
                        <div class="content">
                            <h1>Crafting Strategies That Drive Business Growth</h1>
                            <p>
                                We help manufacturing companies improve efficiency, reduce defects, strengthen supply-chain performance, and scale operations through data-driven strategies and Industry 4.0 solutions.
                            </p>
                            <a href="#" class="bannerButton">
                                Talk to an Expert
                                <img src="/assets/image/gear.gif" alt="">
                            </a>
                        </div>
                    </div>
                </div>

            </div>
            <video class="w-100 plyr-video-player" autoplay loop muted playsinline webkit-playsinline controlslist="nodownload" preload="auto">
                <source src="/assets/image/industryVideo.mp4" type="video/mp4">
            </video>
            <div class="gradient-overlay"></div>

        </div>

        <!-- <ClientSlider /> -->

        <div class="factorySec">
            <img src="/assets/image/factoryVector.webp" class="factoryVector" alt="">
            <div class="container content mt-5 py-5">
                <div class="row mb-4 pb-5">
                    <div class="col-lg-5">
                        <img src="/assets/image/factoryImg.webp" class="img-fluid w-100" alt="factoryImg">
                    </div>
                    <div class="col-lg-7 ps-4">
                        <h5 class="fw-bold text-uppercase mt-5">Who we are</h5>
                        <h2 class="fw-light mb-0">Building quality through</h2>
                        <h2 class="fw-bold">industrial innovation</h2>
                        <p>
                            We partner with automotive, FMCG, electronics, construction-equipment, and farm-machinery manufacturers to solve complex operational challenges. Our approach blends lean principles, digital integration, and structured improvement systems to help factories operate with higher speed, quality, and stability.
                        </p>
                        <h5>What We Focus On:</h5>
                        <div class="row">
                            <div class="col-sm-7">
                                <ul class="list">
                                    <li>
                                        Establish itself as a trusted transformation partner in the automotive ecosystem
                                    </li>
                                    <li>
                                        Scale from project-based consulting to long-term, end to end transformation engagements
                                    </li>
                                    <li>
                                        Build strong, differentiated capability in Lean, TQM, TPM, Digital Manufacturing and Leadership Development
                                    </li>

                                </ul>
                            </div>
                            <div class="col-sm-5">
                                <div class="ratingSec">
                                    <h2 class="bigFont fw-bold mb-0">4.9</h2>
                                    <img src="/assets/image/5starImg.png" class="img-fluid" alt="">
                                    <p class="mb-0">Client Satisfaction Across 25+ Projects</p>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>

        <ServiceSlider />

        <div class="whiteBg">
            <div class="container py-5">
                <div class="row">
                    <div class="col-sm-12 col-lg-5">
                        <h4 class="gearIcon fw-bold">OUR PROCESS</h4>
                        <h2 class="fw-light">Streamlined processes <span class="fw-bold">for optimal efficiency</span></h2>
                    </div>
                    <div class="col-sm-0 col-lg-1 px-0"></div>
                    <div class="col-sm-12 col-lg-6">
                        <p class="mt-4 pt-2">
                            Our structured consulting approach is built to deliver measurable improvement, reduce operational losses, and create long-term stability across manufacturing environments.
                        </p>
                    </div>
                </div>
                <div class="row mt-sm-4">
                    <div class="col-lg-6 mt-sm-4">
                        <img src="/assets/image/our-process-image.webp" class="ourProcessImage img-fluid pe-lg-5 px-sm-5 w-100" alt="">
                    </div>
                    <div class="col-lg-6">
                        <div class="process">
                            <h2>01</h2>
                            <div>
                                <h5>Scoping & Diagnosis</h5>
                                <p class="fw-light mb-2">
                                    We analyze your processes, study data patterns, and identify gaps that limit throughput, quality, or reliability.
                                </p>
                            </div>
                        </div>
                        <div class="process">
                            <h2>02</h2>
                            <div>
                                <h5>Solution Design</h5>
                                <p class="fw-light mb-2">
                                    We build tailored solutions using lean principles, digital tools, and industry-specific best practices.
                                </p>
                            </div>
                        </div>
                        <div class="process">
                            <h2>03</h2>
                            <div>
                                <h5>Implementation</h5>
                                <p class="fw-light mb-2">
                                    We work on-site with your teams to deploy improvements, stabilize workflows, and strengthen day-to-day operations.
                                </p>
                            </div>
                        </div>
                        <div class="process">
                            <h2>04</h2>
                            <div>
                                <h5>Continuous Improvements</h5>
                                <p class="fw-light mb-2">
                                    We establish review cycles, KPIs, and audits to ensure improvements sustain and scale over time.
                                </p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>

        <div class="container-fluid p-0">
            <img src="/public/assets/image/PrimalSolutionsModels.png" class="img-fluid" alt="">
        </div>

        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">OUR CLIENT SAY</h4>
                    <h2 class="fw-light">What our <span class="fw-bold themeText">satisfied clients</span> are saying</h2>
                </div>
                <div class="col-sm-0 col-lg-1 px-0"></div>
                <div class="col-sm-12 col-lg-6">
                    <p class="mt-4 pt-2">
                        Our clients consistently report improved productivity, faster delivery cycles, and stronger operational stability after working with us.
                    </p>
                </div>
            </div>

            <div class="splide py-sm-4 py-2 story-slider">
                <div class="splide__track py-4">
                    <ul class="splide__list">
                        <li class="splide__slide" v-for="story in stories">
                            <div class="storyCard">
                                <img src="/assets/image/commaImg.png" class="commaImg img-fluid" alt="">
                                <div class="row">
                                    <div class="col-sm-9">
                                        <h4>{{ story?.description }}</h4>
                                    </div>
                                </div>
                                <div class="d-flex align-items-center gap-3">
                                    <img :src="story?.image ? `${story?.image}` : ''" class="userImg img-fluid" alt="">
                                    <div>
                                        <h5 class="fw-bold">{{ story?.name }}</h5>
                                        <img src="/assets/image/starImg.png" class="starImg img-fluid" alt="">
                                    </div>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

        </div>

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
                        Real examples of how we've helped automotive, FMCG, electronics, and industrial clients improve productivity, strengthen quality, and scale performance.
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

        <ContactFormBg />
        <ContactForm />

        <Footer />

    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import { useHead } from '#app'
import { blogs } from '~/data/blogs.js';
import { caseStudies } from '~/data/caseStudies.js';

const stories = ref([
    {
        name: 'Cameron Williamson',
        description: 'I cant describe how great we feel using Newsify. It completely changed our workflow and the face we waste on truying to connect each other.Top Newsify!"',
        image: '/assets/image/usersImg.png',
    },
]);

// Add slick and Splide CSS and JS in head
useHead({
    link: [
        {
            rel: 'stylesheet',
            href: 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css',
        },
        {
            rel: 'stylesheet',
            href: 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.min.css',
        },
        {
            rel: 'stylesheet',
            href: 'https://cdn.jsdelivr.net/npm/@splidejs/splide@4.1.4/dist/css/splide.min.css',
        }
    ],
    script: [
        {
            src: 'https://cdn.jsdelivr.net/npm/@splidejs/splide@4.1.4/dist/js/splide.min.js'
        }
    ]
});

onMounted(() => {
    if (typeof window === 'undefined') return;

    // Wait for Splide to be loaded
    let attempts = 0;
    const checkSplide = () => {
        if (window.Splide) {
            const splide = new window.Splide(".story-slider", {
                drag: "free",
                focus: 0,
                omitEnd: true,
                snap: true,
                arrows: true,
                indicators: true,
                breakpoints: {
                    2600: {
                        perPage: 1,
                    },
                    1440: {
                        perPage: 1,
                    },
                    1024: {
                        perPage: 1,
                    },
                    768: {
                        perPage: 1,
                    },
                    576: {
                        perPage: 1,
                    },
                },
            });
            splide.mount();
            const splide2 = new window.Splide(".blog-slider", {
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
            const splide3 = new window.Splide(".caseStudy-slider", {
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
        } else if (attempts < 50) {
            attempts++;
            setTimeout(checkSplide, 100);
        }
    };
    checkSplide();
});

// SEO Meta Tags
useSeoMeta({
  title: '',
  description: '',
  keywords: ''
})

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.homeBnr {
    position: relative;
}
.homeBnr h1{
    color: #fff;
}

.homeBnr .content {
    height: 100vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 2;
}

.homeBnr .content h1 {
    font-size: 60px;
}

.homeBnr video {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100%;
    object-fit: cover;
    z-index: 0;

}
.gradient-overlay {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100%;
    background: linear-gradient(to right, rgb(0, 0, 0, 0.7), rgb(0, 0, 0, 0.1));
    z-index: 1;
}
.bannerButton{
    color: #111F61;
    background-color: #fff;
    border-radius: 50px;
    padding: 8px 10px 8px 15px;
    display: flex;
    align-items: center;
    gap: 6px;
    width: max-content;
    text-decoration: none;
}
.bannerButton img{
    width: 35px;
}

.factorySec {
    position: relative;
}
.factorySec .content{
    position: relative;
    z-index: 2;
}
.factorySec .factoryVector {
    position: absolute;
    bottom: 0px;
    left: 0;
    width: 40%;
    z-index: 1;
}

.factorySec .list li{
    position: relative;
    list-style-type: none;
    margin-bottom: 10px;
}
.factorySec .list li::before {
    content: '';
    position: absolute;
    left: -30px;
    top: 15px;
    width: 16px;
    height: 16px;
    transform: translateY(-50%);
    background: url("/assets/image/tickImg.png") no-repeat center;
    background-size: contain;
}
.ratingSec{
    background-color: #fff;
    border-radius: 40px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    text-align: center;
}
.ratingSec h2{
    color: #042589;
}
.ratingSec img{
    width: 80%;
    max-width: 150px;
}
.ourProcessImage{
    aspect-ratio: 767/717;
    object-fit: cover;
}
.process{
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 10px;
    padding: 20px;
    border-radius: 30px;
}
.process h2{
    font-size: 2.5rem;
    margin: 0;
}

.process:hover{
    background-color: #111F61;
    color: #fff;
    transition: 0.4s;
}
.process:hover h2, .process:hover h5, .process:hover p{
    color: #fff;
    transition: 0.3s;
}

.storyCard{
    background-image: url('/assets/image/testimonialVector.png'),linear-gradient(to bottom, #111F61, #111F61);
    background-repeat: no-repeat;
    background-position: top right;
    background-size: contain;
    color: #fff;
    padding: 30px;
    border-radius: 35px;
    margin: 0 6px;
    position: relative;
}
.storyCard .userImg{
    width: 40px;
    height: 40px;
    aspect-ratio: 1/1;
    border-radius: 50%;
}
.storyCard h4{
    color: #fff;
    line-height: 1.8;
    margin-top: 10px;
    margin-bottom: 50px;
}
.storyCard h5{
    color: #fff;
    margin-bottom: 0;
}
.storyCard .starImg{
    width: 80px;
}
.storyCard .commaImg{
    position: absolute;
    bottom: 10%;
    right: 4%;
    width: 20%;
    max-width: 150px;
    margin-bottom: 10px;
}




@media only screen and (max-width:1440px) {

}
@media only screen and (max-width:1280px) {
    .homeBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .homeBnr .content h1 {
        font-size: 44px;
    }
}
@media only screen and (max-width: 830px) {
    .homeBnr .content h1 {
        font-size: 40px;
    }

}
@media only screen and (max-width:578px) {

}

</style>
