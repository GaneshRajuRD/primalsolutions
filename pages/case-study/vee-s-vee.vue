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
                                Redefining Bar Machining Performance Through Zero-Defect Culture
                            </h1>
                            <p class="mb-5 mb-lg-0">6 min read</p>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="csBnrImgSec">
                            <img src="/assets/image/zero defect culture.webp" class="img-fluid csBnrImg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5 caseStudyContent mb-5">
            <h4>Overview</h4>
            <p>
                A leading bar machining manufacturing company in Chennai, supplying precision-engineered components to the commercial vehicle industry, recognized the need to enhance operational efficiency and improve its supplier performance ranking with a major OEM. Persistent quality complaints, delivery failures, and rising customer expectations were impacting business growth and competitiveness.
            </p>
            <h4>The Challenge</h4>
            <p>
                The organization was facing multiple operational and quality-related challenges that were impacting overall performance: 
            </p>
            <ul>
                <li>Recurring customer quality complaints and process inconsistencies</li>
                <li>On-time delivery failures leading to reduced supplier ratings and strained customer relationships</li>
                <li>Inefficient production planning causing schedule delays and high WIP</li>
                <li>Weak quality control systems with inadequate in-process inspection</li>
                <li>Poor traceability and reactive defect handling</li>
                <li>Increasing pressure to achieve zero-defect and faster response standards</li>
            </ul>
            <!-- <img src="/assets/image/caseStudy.webp" class="img-fluid w-100" alt=""> -->
            <h4>Strategic Actions & Business Impact</h4>
            <p>
                To overcome these challenges, the organization partnered with Primal Solutions to design and execute a structured transformation roadmap focused on the following key priorities: 
                  Strengthened incoming inspection with firewall controls and Q-Gates under the structured "3D" quality concept prevented defect escape, strengthened incoming quality control, and reduced customer complaints. Structured Daily Work Management (DWM) Implementation increased leadership visibility, improved daily performance tracking, and accelerated decision-making.
            </p>
            <h6>Comprehensive Operational Assessment</h6>
            <p>Identified critical productivity losses, quality leakages, planning gaps, enabling focused corrective actions.</p>
            <h6>CNC Shopfloor Layout Redesign</h6>
            <p>Improved material flow, reduced movement waste, enhanced machine utilization and output.</p>
            
            <h4>Strategic Outcome</h4>
            <p>
                The organization transitioned from a reactive quality system to a structured Zero-Defect culture, significantly strengthening its supplier performance position and unlocking new business opportunities including NPD engagement.
            </p>

            <div class="table-responsive mt-4">
                <table class="table performanceTable">
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Before</th>
                            <th>After</th>
                            <th>Change / Impact</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Supplier Performance Ranking</td>
                            <td>Low</td>
                            <td>Moderate</td>
                            <td>↑ Potential to reach high performance</td>
                        </tr>
                        <tr>
                            <td>CPI Instances</td>
                            <td>High</td>
                            <td>Low</td>
                            <td>50% drop in COPQ</td>
                        </tr>
                        <tr>
                            <td>Green Channel Parts</td>
                            <td>92%</td>
                            <td>99%</td>
                            <td>Expanded business share and unlocked new product development opportunities</td>
                        </tr>
                        <tr>
                            <td>Delivery Performance</td>
                            <td>70%</td>
                            <td>84%</td>
                            <td>20% Increase in Topline Revenue</td>
                        </tr>
                        <tr>
                            <td>Operational Efficiency</td>
                            <td>-</td>
                            <td>20%</td>
                            <td>Streamlined CNC layout and minimized inventory levels</td>
                        </tr>
                    </tbody>
                </table>
            </div>

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
    {
        title: 'Zero-Defect Cultural Transformation',
        videoUrl: '/assets/image/Zero-Defect Cultural Transformation.mp4',
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

.performanceTable {
    background: linear-gradient(to right, #2c3e50, #1f2937);
    color: #fff;
    /* border-radius: 15px; */
    overflow: hidden;
}

.performanceTable th {
    background-color: #2b4c7e;
    font-weight: 600;
    color: #fff;
    border: 1px solid rgba(255,255,255,0.2);
}

.performanceTable td {
    border: 1px solid #e1e1e1;
    vertical-align: middle;
}

.performanceTable tr:hover {
    border: 1px solid #e1e1e1;
    background-color: rgba(255,255,255,0.05);
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

