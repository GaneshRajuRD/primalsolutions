<template>
    <div>
        <Header />

        <div class="csBnr">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="content">
                            <span class="bnrTag">CASE STUDY</span>
                            <h1 class="my-4">
                                Transforming Production Efficiency for a Leading Sheet Metal Manufacturer in Hosur
                            </h1>
                            <p class="mb-5 mb-lg-0">5 min read</p>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="csBnrImgSec">
                            <img src="/assets/image/caseStudyImg.webp" class="img-fluid csBnrImg" />
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <div class="container py-5 caseStudyContent mb-5">
            <h4>The Company</h4>
            <p>
                A leading sheet metal manufacturing company based in Hosur, specializing in a diverse range of sheet metal and press components for commercial vehicles, defense vehicles, off-road vehicles, and the electrical and electronics sectors, set out to enhance its production efficiency and streamline operations. As demand increased, the company recognized the need to optimize its manufacturing processes to boost productivity, improve quality, and reduce operational costs.
            </p>
            <h4>The Challenge</h4>
            <p>
                With rising demand, the company encountered several operational challenges, including inefficient material flow, frequent production bottlenecks, customer complaints related to quality issues, excessive inventory levels, and extended lead times. These issues hampered productivity, escalated operational costs, and restricted the company’s ability to scale and meet customer expectations.
            </p>
            <img src="/assets/image/caseStudy.webp" class="img-fluid w-100" alt="">
            <h4>The  Solution</h4>
            <p>
                To drive operational transformation, the company partnered with Primal Solutions, leveraging their expertise to redesign the production layout for improved material flow, reduced redundancies, and lower Cost of Poor Quality (COPQ). Through a comprehensive on-site analysis, Primal Solutions identified key inefficiencies—such as bottlenecks, high inventory, and long lead times—and implemented an optimized layout that significantly enhanced operational efficiency. Leadership played a pivotal role in the success of these initiatives, actively engaging in and supporting the transformation process to ensure optimal results.
            </p>
            <h4>The  Result</h4>
            <img src="/assets/image/caseStudy2.webp" class="img-fluid w-100" alt="">
        </div>

        <div class="realResultsSec py-5">
            <div class="container">
                <h2 class="realResultsTitle mb-5">Real Results in <span class="fw-bold">Motion</span></h2>
                <VideoTabs :videos="videos" />
            </div>
        </div>

        <Footer />
        
    </div>
</template>
<script setup>
import { onMounted } from "vue";

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