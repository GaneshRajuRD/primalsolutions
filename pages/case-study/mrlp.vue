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
                                Transforming a Legacy Automotive Supplier for Future-Ready Growth
                            </h1>
                            <p class="mb-5 mb-lg-0">5 min read</p>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="csBnrImgSec">
                            <img src="/assets/image/Transforming legacy automotive supplier for furture growth.webp" class="img-fluid csBnrImg" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5 caseStudyContent mb-5">

            <h4>Background</h4>
            <p>
                With a strong 60-year legacy, a Chennai-based automotive supplier manufactures fuel tanks and sheet metal components for a wide spectrum of vehicles, including commercial vehicles, farm equipment, two-wheelers, passenger cars, and electric vehicles. Confronted by rising customer expectations and a rapidly diversifying product portfolio, the company identified the critical need to scale up operations, improve quality, and boost operational efficiency to stay ahead in a competitive market.
            </p>

            <h4>The Challenge</h4>
            <p>To achieve its ambitious growth plans for FY25–FY28, the company set out to:</p>
            <ul>
                <li>Rapidly adapt to shifting customer requirements and market trends</li>
                <li>Upgrade product quality and streamline operational efficiency</li>
                <li>Strengthen organizational capabilities to support ongoing growth and diversification</li>
            </ul>


            <h4>The Solution</h4>
            <p>
                To drive this transformation, the company partnered with Primal Solutions. The engagement began with in-depth market research, yielding valuable insights into industry trends and customer preferences. These insights were instrumental in shaping a focused business plan, closely aligned with the company’s vision, mission, and long-term strategic goals.
            </p>

            <h5>Key initiatives:</h5>
            <h6>KPI & KRA Framework</h6>
            <p>
                Defined clear performance metrics to ensure accountability and transparency.
            </p>

            <h6>Organizational Assessment</h6>
            <p>
                Evaluated operations and competencies to design a future-ready structure.
            </p>

            <h6>Departmental Transformation</h6>
            <p>
                Implemented targeted strategies, training, and performance systems to build a high-performance culture.
            </p>

            <h4 class="mt-5">Results & Business Impact</h4>

            <div class="table-responsive mt-4">
                <table class="table performanceTable">
                    <thead>
                        <tr>
                            <th>Focus Area</th>
                            <th>Key Impact</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Quality Enhancements</td>
                            <td>In-house PPM reduced by 50%; COPQ lowered from 0.3% to 0.1%</td>
                        </tr>
                        <tr>
                            <td>Process Optimization</td>
                            <td>Fuel tank assembly line efficiency and quality significantly improved</td>
                        </tr>
                        <tr>
                            <td>Benchmarking Excellence</td>
                            <td>Established a model fabrication & assembly line for the EV Auto segment, setting new industry benchmarks</td>
                        </tr>
                        <tr>
                            <td>New Product Development</td>
                            <td>Achieved 100% First Time Right; tooling upgrades and value engineering delivered major cost savings</td>
                        </tr>
                        <tr>
                            <td>Inspection Facility Upgrade</td>
                            <td>Transformed standard room into a state-of-the-art, OEM-compliant inspection facility with standardized single-piece design</td>
                        </tr>
                    </tbody>
                </table>
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
  title: 'MRLP Case Study | Primal Solutions',
  meta: [
    { name: 'description', content: 'MRLP case study showing automotive supply chain transformation and manufacturing improvement.' },
    { name: 'keywords', content: 'MRLP case study, automotive transformation, manufacturing performance' }
  ]
})
import { onMounted } from "vue";

const videos = ref([
    // {
    //     title: 'Plant Layout Transformation',
    //     videoUrl: '/assets/image/Plant Layout Transformation.mp4',
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

