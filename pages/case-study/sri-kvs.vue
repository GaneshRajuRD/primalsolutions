<template>
    <div>
        <Header />
        <Loader />

        <div class="csBnr">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="content">
                            <span class="bnrTag">CASE STUDY</span>
                            <h1 class="my-4">
                                30-Day Rapid Plant Layout Transformation for a Precision Machining Manufacturer
                            </h1>
                            <p class="mb-5 mb-lg-0">5 min read</p>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="csBnrImgSec">
                            <img src="/assets/image/30 day rapid 1.webp" class="img-fluid csBnrImg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5 caseStudyContent mb-5">
            <h4>Client Overview</h4>
            <p>
                A leading manufacturer of precision turned, machined, and forged components, and a long-standing supplier to Ashok Leyland for over three decades, partnered with Primal Solutions to accelerate operational excellence and future-ready growth.
            </p>
            <h4>The Business Challenge</h4>
            <p>
                With increasing customer expectations and ambitious expansion plans, the organization set out to achieve a complete end-to-end operational transformation—within an aggressive 30-day timeline. The leadership team identified the following priorities:
            </p>
            <ul>
                <li>Comprehensive plant layout optimization based on detailed shopfloor study</li>
                <li>Improved end-to-end functional efficiency</li>
                <li>Higher operational productivity</li>
                <li>Stronger foundation for scalable growth</li>
            </ul>
            <!-- <img src="/assets/image/caseStudy.webp" class="img-fluid w-100" alt=""> -->
            <h4>Our Transformation Approach</h4>
            <p>
                Primal Solutions deployed a dedicated rapid-transformation task force comprising domain experts across manufacturing, layout engineering, and operational excellence. Over a structured 30-day intervention, we executed: 
            </p>
            <ul>
                <li>In-depth current-state layout study and bottleneck analysis</li>
                <li>Scientific layout redesign to streamline material flow</li>
                <li>Cross-functional process optimization</li>
                <li>Functional alignment with clear performance accountability</li>
                <li>Discipline-driven execution model to ensure measurable impact</li>
            </ul>
            <h4>Results Delivered — Within 30 Days</h4>
            <p>
                The focused intervention generated immediate and measurable outcomes: 
            </p>
            <ul>
                <li>Significant improvement in operational efficiency</li>
                <li>Optimized plant layout enabling seamless material movement</li>
                <li>20% topline growth driven by productivity enhancement</li>
                <li>Expanded customer base and stronger market positioning</li>
                <li>Recognition with the Ashok Leyland National Supplier Samrat Award, reinforcing supplier excellence</li>
            </ul>
            <img src="/assets/image/caseStudy2.webp" class="img-fluid w-100" alt="">
            <h4>Business Impact</h4>
            <p>
                The 30-day transformation positioned the organization for scalable growth, improved competitiveness, and stronger operational control. This demonstrates that with structured methodology, expert-led execution, and disciplined implementation, measurable transformation can be achieved within a compressed timeframe—strengthening the company's position as a preferred supplier to leading OEMs.
            </p>

            <div class="row">
                <div class="col-md-6 col-lg-4">
                    <img src="/assets/image/30 day rapid 2.webp" class="csImg img-fluid w-100" alt="">
                </div>
                <div class="col-md-6 col-lg-4">
                    <img src="/assets/image/30 day rapid 3.webp" class="csImg img-fluid w-100" alt="">
                </div>
                <div class="col-md-6 col-lg-4">
                    <img src="/assets/image/30 day rapid 3.webp" class="csImg img-fluid w-100" alt="">
                </div>
            </div>

        </div>

        <div class="realResultsSec py-5" v-if="videos.length > 0">
            <div class="container">
                <h2 class="realResultsTitle mb-5">Real Results in <span class="fw-bold">Motion</span></h2>
                <VideoTabs :videos="videos" />
            </div>
        </div>

        <ContactFormBg />
        <ContactForm />
        <Footer />
        
    </div>
</template>
<script setup>
import { useHead } from '#app'
useHead({
  title: 'Sri KVS Case Study | Primal Solutions',
  meta: [
    { name: 'description', content: 'Sri KVS case study demonstrating plant layout improvement and operational efficiency in manufacturing.' },
    { name: 'keywords', content: 'Sri KVS case study, plant layout improvement, manufacturing efficiency' }
  ]
})
import { onMounted } from "vue";

const videos = ref([
    {
        title: 'Plant Layout Transformation',
        videoUrl: '/assets/image/Plant Layout Transformation.mp4',
    },
]);

</script>
<style scoped>
.csBnr {
    background-image: url('/assets/image/caseStudyVector.png'),linear-gradient(to right,rgb(20, 69, 146),rgb(57, 63, 74));
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}

.csBnr .content{
    color: #fff;
    height: 100vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
}

.csBnr .content h1{
    color: #fff;
    font-size: 48px;
    font-weight: 300;
}

.csBnr .bnrTag{
    background-color: rgb(255, 255, 255,0.3);
    padding: 5px 10px;
    color: #fff;
    border-radius: 5px;
    width: max-content;
}
.csBnrImgSec{
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.csBnrImgSec img{
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
    border-radius: 20px;
}
.caseStudyContent p{
    margin-bottom: 25px;
}

.caseStudyContent img{
    border-radius: 25px;
    margin: 20px 0;
}

.realResultsSec {
    background-color: #F0F3FF;
}

.realResultsTitle {
    font-size: 48px;
    margin-bottom: 3rem;
}

.csImg{
    aspect-ratio: 810/610;
    object-fit: cover;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    
}
@media only screen and (max-width:1080px) {
    .realResultsTitle {
        font-size: 36px;
    }
}
@media only screen and (max-width:830px) {
    .csBnr .content{
        width: 100%;
    }
    .csBnr .content h1{
        font-size: 30px;
    }
}
@media only screen and (max-width:578px) {
    
}
</style>

