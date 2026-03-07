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
                                Driving Supplier Excellence Under OEM Quality Benchmark Program
                            </h1>
                            <p class="mb-5 mb-lg-0">7 min read</p>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="csBnrImgSec">
                            <img src="/assets/image/Driving Supplier Excellence Under OEM Quality Benchmark Program.webp" class="img-fluid csBnrImg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5 caseStudyContent mb-5">
            <h4>Client Overview</h4>
            <p>
                A well-established sheet metal fabrication manufacturer with over five decades of expertise in Truck Cabins, Front End Structures (FES), Tipper Bodies, and Stamping Weldments was identified as one of 20 strategic partners under a leading commercial truck OEM's Quality Initiative Program.
            </p>
            <h4>The Challenge</h4>
            <p>
                While the organization possessed strong technical capabilities and a solid market reputation, its Supplier Process Audit score remained at a moderate level, indicating gaps in quality governance, assembly flow efficiency, and performance visibility.
            </p>
            <!-- <img src="/assets/image/caseStudy.webp" class="img-fluid w-100" alt=""> -->
            <h4>Our Approach</h4>
            <p>
                To bridge these gaps, a structured transformation program was initiated with a focused objective: elevate supplier performance to a high-performance benchmark, secure "Quality Challenger" recognition, and strengthen assembly capability through robust, system-driven practices. Primal Solutions implemented a comprehensive improvement framework beginning with a detailed baseline assessment. Key gaps were systematically addressed through enhanced inspection controls, disciplined review mechanisms, and strengthened accountability structures.
            </p>
            <p>
                Assembly layouts were strategically redesigned to eliminate non-value-added movement, streamline material flow, and improve line balancing—significantly enhancing truck cabin assembly efficiency and overall shopfloor productivity. 
            </p>
            <p>
                To ensure long-term sustainability, a KPI-led governance model was introduced. Daily Work Management (DWM) practices and structured visual management systems were institutionalized, driving transparency, ownership, and real-time performance monitoring across operations.
            </p>
            <h4>Outcome</h4>
            <p>
                The initiative resulted in a clear upward trajectory in supplier performance score, improved audit readiness, stronger alignment with OEM expectations, and a sustainable roadmap toward achieving and maintaining high-performance benchmark standards—positioning the organization for scalable growth in FY26 and beyond.
            </p>
            <!-- <img src="/assets/image/caseStudy2.webp" class="img-fluid w-100" alt=""> -->
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
import { onMounted } from "vue";

const videos = ref([
    // {
    //     title: 'Supplier Excellence Overview',
    //     videoUrl: '/assets/image/industryVideo.mp4',
    // },
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

