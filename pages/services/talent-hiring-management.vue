<template>
    <div>
        <Header />

        <div class="serviceBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-bold">Talent Hiring & Management</h1>
                    <p class="width-75">
                        We help you hire the right people, build structured evaluation systems, and keep teams aligned and engaged.
                    </p>
                </div>
            </div>
        </div>

        <div class="deliverablesSec">
            <div class="container">
                <div class="deliverables">
                    <div class="delivery1">
                        <h5 class="mb-0">What We Deliver:</h5>
                    </div>
                    <div class="delivery2">
                        <div class="content">
                            <img src="/assets/image/tickImg3.png" class="tickImg img-fluid" alt="">
                            <p class="mb-0">Role-based hiring systems</p>
                        </div>
                    </div>
                    <div class="delivery2">
                        <div class="content">
                            <img src="/assets/image/tickImg3.png" class="tickImg img-fluid" alt="">
                            <p class="mb-0">Structured evaluation frameworks</p>
                        </div>
                    </div>
                    <div class="delivery2">
                        <div class="content">
                            <img src="/assets/image/tickImg3.png" class="tickImg img-fluid" alt="">
                            <p class="mb-0">Retention & onboarding support</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container my-5">
            <div class="row">
                <div class="col-sm-4 col-lg-5">
                    <img src="/assets/image/serviceImg1.webp" class="mt-sm-5 mt-lg-0  img-fluid w-100" alt="">
                </div>
                <div class="col-sm-8 col-lg-7 ps-xl-5 mt-5 pt-xl-4">
                    <span class="tag">What we do</span>
                    <h1 class="playfairText themeText mt-3">Strengthen your workforce pipeline</h1>
                    <p>
                        We create hiring and talent systems that support strong operational performance. From screening to onboarding, we ensure each new hire matches the skills, behavior, and expectations needed for the role.
                    </p>
                    <ul class="strengthList">
                        <li>Hire talent aligned to operational needs</li>
                        <li>Build structured evaluation and screening flows</li>
                        <li>Improve retention with clear role expectations</li>
                    </ul>
                </div>
            </div>
        </div>


        <div ref="textSlider" class="textSlider">
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
            <div class="text-item">Building High-Performance Teams</div>
        </div>

        <div class="container py-5">
            <span class="tag">Real World Impact</span>
            <h1 class="playfairText themeText mt-3">Turning Strategy Into Real Progress</h1>

            <div class="row mt-4">
                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <div class="strategyCard">
                        <img src="/assets/image/tickImg5.png" class="img-fluid" alt="">
                        <h5 class="fw-light">
                            31% faster hiring cycles
                        </h5>
                    </div>
                </div>
                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <div class="strategyCard">
                        <img src="/assets/image/tickImg5.png" class="img-fluid" alt="">
                        <h5 class="fw-light">
                            36% improvement in role fit accuracy
                        </h5>
                    </div>
                </div>
                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <div class="strategyCard">
                        <img src="/assets/image/tickImg5.png" class="img-fluid" alt="">
                        <h5 class="fw-light">
                            22% drop in early-stage attrition
                        </h5>
                    </div>
                </div>
                <div class="col-sm-6 col-lg-4 col-xl-3">
                    <div class="strategyCard">
                        <img src="/assets/image/tickImg5.png" class="img-fluid" alt="">
                        <h5 class="fw-light">
                            Higher team stability and engagement
                        </h5>
                    </div>
                </div>
            </div>
        </div>

        <div class="lightBlueBg py-5">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <h4 class="gearIcon fw-bold">OUR PROCESS</h4>
                        <h1 class="playfairText themeText">How We Transform <br> Operations</h1>
                        <div class="accordionSec">
                            <Accordion :accordions="operations" />
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <img src="/assets/image/operationsImg.webp" class="img-fluid w-100" alt="">
                    </div>
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

        
        <div class="realResultsSec py-5">
            <div class="container">
                <h2 class="realResultsTitle mb-5">Real Results in <span class="fw-bold">Motion</span></h2>
                <VideoTabs :videos="videos" />
            </div>
        </div>

        <ContactFormBg />
        <ContactForm />

        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">FAQS</h4>
                    <h2 class="fw-light">Frequently asked <br><span class="fw-bold">questions</span></h2>
                </div>
            </div>

            <div class="row">
                <div class="col-lg-6 pe-lg-5 mt-4">
                    <div class="faqImg">
                        <img src="/assets/image/faqImg.webp" class="w-100 img-fluid" alt="">
                        <div class="contact">
                            <a href="#">
                                <img src="/assets/image/callIcon.png" class="img-fluid" alt="">
                                +91 1236547890
                            </a>
                            <a href="#">
                                <img src="/assets/image/mailIcon.png" class="img-fluid" alt="">
                                info@domainname.com
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <Faq v-model:faqs="faqs" class="mt-5 pt-4" />
                </div>
            </div>
        </div>

        <Footer />

        
    </div>
</template>
<script setup>
import { onMounted, ref, nextTick } from "vue";
import Accordion from "~/components/Accordion.vue";
import { caseStudies } from '~/data/caseStudies.js';

const textSlider = ref(null);

const videos = ref([
    {
        title: 'Strategy Implementation Overview',
        videoUrl: '/assets/image/industryVideo.mp4',
    },
    {
        title: 'Real-World Case Study',
        videoUrl: '/assets/image/homeBnrVideo.mp4',
    },
]);

const operations = ref([
    {
        question: 'Scoping & Diagnosis',
        answer: 'We study your processes, people, and performance data to identify gaps and opportunities.',
    },
    {
        question: 'Solution Design',
        answer: 'We create structured, practical solutions tailored to your operational needs.',
    },
    {
        question: 'Implementation & Optimization',
        answer: 'We work hands-on with your teams to deploy improvements and stabilize workflows.',
    },
    {
        question: 'Continual Improvements',
        answer: 'We refine systems, review KPIs, and support long-term sustainability.',
    },
]);

const faqs = ref([
    {
        question: 'What industries do you serve?',
        answer: 'We work with automotive, electronics, FMCG, construction equipment, agricultural machinery, and other manufacturing-driven sectors.',
    },
    {
        question: 'How do you ensure product quality?',
        answer: 'We implement rigorous quality and process controls at every stage of execution, ensuring consistency, compliance, and reliable outcomes.',
    },
    {
        question: 'What sustainability practices do you follow?',
        answer: 'We support ESG-focused improvements by promoting efficient resource use, waste reduction, responsible operations, and long-term environmental practices.',
    },
    {
        question: 'Do you offer customized solutions?',
        answer: 'Yes. Every solution is tailored to your plant, processes, workforce capability, and long-term operational goals.',
    },
    {
        question: 'How do you handle safety in the workplace?',
        answer: 'We follow strict safety standards, structured audits, and compliance protocols to help maintain safe, secure, and well-governed work environments.',
    },
]);

onMounted(async () => {
    const jQueryScript = document.createElement('script');
    jQueryScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js';
    jQueryScript.onload = () => {
        const slickScript = document.createElement('script');
        slickScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js';
        slickScript.onload = () => {
            if (textSlider.value) {
                $(textSlider.value).slick({
                    infinite: true,
                    slidesToScroll: 1,
                    autoplay: true,
                    autoplaySpeed: 0,
                    speed: 10000,
                    pauseOnHover: false,
                    arrows: false,
                    dots: false,
                    cssEase: 'linear',
                    variableWidth: true,
                    draggable: false,
                    swipe: false,
                    touchMove: false
                });
            }
        };
        document.head.appendChild(slickScript);
    };
    document.head.appendChild(jQueryScript);

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
.serviceBnr {
    position: relative;
    background-image: linear-gradient(68deg,rgb(0, 0, 0, 0.5),rgb(0, 0, 0,0)),url('/assets/image/Talent-Hiring-Management-service.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
.serviceBnr h1{
    color: #fff;
}
.serviceBnr .content {
    height: 90vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}
.serviceBnr .content h1 {
    font-size: 60px;
}

.deliverablesSec{
    padding: 25px;
    background-image: linear-gradient(-167deg,#F3F5F8 0%,  #A9BFF8 100%);
}
.deliverables{
    display: flex;
    justify-content: space-between;
}
.deliverables .delivery1, .deliverables .delivery2{
    width: 25%;
}

.deliverablesSec p{
    color: #000;
}
.deliverablesSec .tickImg{
    width: 20px;
    aspect-ratio: 1/1;
}
.deliverables .content{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
}

.faqImg{
    position: relative;
}
.faqImg .contact{
    width: max-content;
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: row;
    gap: 20px;
}
.faqImg .contact a{
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: #fff;
}
.faqImg .contact img{
    width: 20px;
    height: 20px;
    object-fit: contain;
}

::v-deep(.caseStudyCard){
    background-color: #FCFCFD;
    border: 3px solid #F7F7F8;
}
.accordionSec{
    width: 95%;
}
.strategyCard{
    padding: 1.4em;
    border: 1px solid rgb(0, 0, 0, 0.1);
    border-radius: 8px;
    height: calc(100% - 20px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 20px;
}
.strategyCard:hover{
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease-in-out;
}
.strategyCard img{
    width: 25px;
    aspect-ratio: 1/1;
    object-fit: contain;
    margin-bottom: 40px;
}
.strategyCard h5{
    color: #000;
    line-height: 1.6;
    width: 80%;
    margin-bottom: 0;
}

.textSlider {
    color: rgb(27, 39, 61, 0.2);
    padding: 15px 0;
    overflow: hidden;
    position: relative;
    width: 100%;
}

.text-item {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
    display: inline-block !important;
    opacity: 0.7;
    white-space: nowrap;
    font-size: 14vh;
    padding: 0 6rem;
    text-align: center;
    position: relative;
    line-height: 1.3;
    margin: 0;
}

.textSlider .text-item::before {
    position: absolute;
    content: '';
    width: 12vh;
    height: 12vh;
    border-radius: 50%;
    background-color: #728AEC;
    left: -6vh;
    top: 50%;
    transform: translate(0%, -50%);
}

/* Slick slider overrides */
.textSlider .slick-track {
    display: flex;
    align-items: center;
}

.textSlider .slick-slide {
    height: auto;
}

.textSlider .slick-list {
    overflow: hidden;
}

.textSlider .slick-arrow {
    display: none !important;
}

.textSlider .slick-dots {
    display: none !important;
}

/* Real Results in Motion Section */
.realResultsSec {
    background-color: #F0F3FF;
}

.realResultsTitle {
    font-size: 48px;
    margin-bottom: 3rem;
}

.tag{
    background-color: #F1F2F5;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 15px;
}
.strengthList li{
    position: relative;
    list-style-type: none;
    line-height: 2.4;
}
.strengthList li::before {
    content: '';    
    position: absolute;
    left: -30px;
    top: 50%;
    width: 16px;
    height: 16px;
    transform: translateY(-50%);
    background: url("/assets/image/tickImg4.png") no-repeat center;
    background-size: contain;
}


@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    .serviceBnr .content h1 {
        font-size: 50px;
    }
    .deliverablesSec p{
        font-size: 15px;
    }
}
@media only screen and (max-width:1080px) {
    .serviceBnr .content h1 {
        font-size: 44px;
    }
    .realResultsTitle {
        font-size: 36px;
    }
}
@media only screen and (max-width:830px) {
    .serviceBnr .content h1 {
        font-size: 40px;
    }
    .deliverables{
        flex-wrap: wrap;
    }
    .deliverables .delivery1{
        width: 100%;
        padding: 5px 0;
    }
    .deliverables .delivery2{
        width: 33%;
        padding: 5px 0;
    }
    .deliverables .content{
        justify-content: start;
        gap: 12px;
    }
    .footerMarquee{
        font-size: 8vh;
    }
    .strategyCard h5{
        width: 100%;
    }
    .text-item{
        font-size: 8vh;
        padding: 0 4rem;
    }
    .textSlider .text-item::before {
        width: 6vh;
        height: 6vh;
        left: -3vh;
    }
    .accordionSec{
        width: 100%;
        margin: 25px 0;
    }
}
@media only screen and (max-width:578px) {
    .deliverables .delivery2{
        width: 100%;
    }
    .footerMarquee{
        font-size: 7vh;
    }
    .text-item{
        font-size: 5vh;
        padding: 0 3rem;
    }
    .textSlider .text-item::before {
        width: 4vh;
        height: 4vh;
        left: -2vh;
    }
    .strengthList li {
        position: relative;
        list-style-type: none;
        line-height: 1.7;
    }
    .strengthList li::before{
        top: 30%;
    }
}
</style>
