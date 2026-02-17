<template>
    <div class="body">
        <Header />
        <Loader />

        <div class="aboutUsBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-light">About <span class="fw-bold">Us</span></h1>
                    <p>
                        We help manufacturing companies to enhance operational efficiency, develop strategies, and deliver
measurable results that directly impact the bottom line.
                    </p>
                </div>
            </div>
        </div>

        <ClientSlider />

        <div class="factorySec">
            <img src="/assets/image/factoryVector.webp" class="factoryVector" alt="">
            <div class="container content mt-5 py-5">
                <div class="row mb-4 pb-5">
                    <div class="col-sm-5">
                        <img src="/assets/image/factoryImg.webp" class="img-fluid w-100" alt="factoryImg">
                    </div>
                    <div class="col-sm-7 ps-lg-5 ps-sm-4">
                        <h5 class="fw-bold text-uppercase mt-5">Who we are</h5>
                        <!-- <h2 class="fw-light mb-0">Building quality through</h2>
                        <h2 class="fw-bold">industrial innovation</h2> -->
                        <p>
                            Primal Solutions is a consulting firm serving as a catalysts for <strong>”Organization’s Cultural Transformation”.</strong>
Our focus is on fostering growth and innovation in the automotive sector by working closely with OEMs,
Tier-1 suppliers, and component manufacturers.
                        </p>
                        <div class="numerics">
                            <div class="row">
                                <div class="col-4">
                                    <h3>15+</h3>
                                    <h5>Happy Clients</h5>
                                </div>
                                <div class="col-4">
                                    <h3>3+</h3>
                                    <h5>Cities</h5>
                                </div>
                                <div class="col-4">
                                    <h3>25+</h3>
                                    <h5>Projects</h5>
                                </div>
    
                            </div>
                        </div>
    
                    </div>
                </div>
            </div>
        </div>

        <ContactFormBg />

        <div class="container">
            <div class="missionSec">
                <div class="mission-tabs nav nav-tabs" role="tablist">
                    <button class="tab-btn nav-link active" data-bs-toggle="tab" data-bs-target="#nav-Vision"
                        type="button" role="tab" aria-controls="nav-Vision" aria-selected="false" id="nav-Vision-tab">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.28683 2.42871C5.49973 2.42871 2.42969 5.49876 2.42969 9.28585C2.42969 13.0729 5.49973 16.143 9.28683 16.143C13.0739 16.143 16.144 13.0729 16.144 9.28585C16.144 5.49876 13.0739 2.42871 9.28683 2.42871ZM0.429688 9.28585C0.429688 4.39419 4.39517 0.428711 9.28683 0.428711C14.1785 0.428711 18.144 4.39419 18.144 9.28585C18.144 14.1775 14.1785 18.143 9.28683 18.143C4.39517 18.143 0.429688 14.1775 0.429688 9.28585Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M30.7165 2.42871C26.9294 2.42871 23.8594 5.49876 23.8594 9.28585C23.8594 13.0729 26.9294 16.143 30.7165 16.143C34.5036 16.143 37.5737 13.0729 37.5737 9.28585C37.5737 5.49876 34.5036 2.42871 30.7165 2.42871ZM21.8594 9.28585C21.8594 4.39419 25.8249 0.428711 30.7165 0.428711C35.6082 0.428711 39.5737 4.39419 39.5737 9.28585C39.5737 14.1775 35.6082 18.143 30.7165 18.143C25.8249 18.143 21.8594 14.1775 21.8594 9.28585Z" fill="#222222"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.28683 23.8572C5.49973 23.8572 2.42969 26.9272 2.42969 30.7143C2.42969 34.5014 5.49973 37.5715 9.28683 37.5715C13.0739 37.5715 16.144 34.5014 16.144 30.7143C16.144 26.9272 13.0739 23.8572 9.28683 23.8572ZM0.429688 30.7143C0.429688 25.8227 4.39517 21.8572 9.28683 21.8572C14.1785 21.8572 18.144 25.8227 18.144 30.7143C18.144 35.606 14.1785 39.5715 9.28683 39.5715C4.39517 39.5715 0.429688 35.606 0.429688 30.7143Z" fill="#222222"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M30.7165 23.8572C26.9294 23.8572 23.8594 26.9272 23.8594 30.7143C23.8594 34.5014 26.9294 37.5715 30.7165 37.5715C34.5036 37.5715 37.5737 34.5014 37.5737 30.7143C37.5737 26.9272 34.5036 23.8572 30.7165 23.8572ZM21.8594 30.7143C21.8594 25.8227 25.8249 21.8572 30.7165 21.8572C35.6082 21.8572 39.5737 25.8227 39.5737 30.7143C39.5737 35.606 35.6082 39.5715 30.7165 39.5715C25.8249 39.5715 21.8594 35.606 21.8594 30.7143Z" fill="#111F61"/>
                        </svg>
                        Our Vision
                    </button>
                    <button class="tab-btn nav-link" data-bs-toggle="tab" data-bs-target="#nav-Mission" type="button"
                        role="tab" aria-controls="nav-Mission" aria-selected="true" id="nav-Mission-tab">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M38.1417 28.5713C38.694 28.5713 39.1417 29.019 39.1417 29.5713V35.2856C39.1417 36.3086 38.7354 37.2897 38.012 38.013C37.2887 38.7364 36.3076 39.1427 35.2846 39.1427H29.5703C29.018 39.1427 28.5703 38.695 28.5703 38.1427C28.5703 37.5905 29.018 37.1427 29.5703 37.1427H35.2846C35.7771 37.1427 36.2495 36.9471 36.5978 36.5988C36.9461 36.2505 37.1417 35.7781 37.1417 35.2856V29.5713C37.1417 29.019 37.5895 28.5713 38.1417 28.5713Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M28.5703 1C28.5703 0.447715 29.018 0 29.5703 0H35.2846C36.3076 0 37.2887 0.406377 38.012 1.12973C38.7354 1.85309 39.1417 2.83416 39.1417 3.85714V9.57143C39.1417 10.1237 38.694 10.5714 38.1417 10.5714C37.5895 10.5714 37.1417 10.1237 37.1417 9.57143V3.85714C37.1417 3.3646 36.9461 2.89223 36.5978 2.54394C36.2495 2.19566 35.7771 2 35.2846 2H29.5703C29.018 2 28.5703 1.55228 28.5703 1Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M3.85714 2C3.3646 2 2.89223 2.19566 2.54394 2.54394C2.19566 2.89223 2 3.3646 2 3.85714V9.57143C2 10.1237 1.55228 10.5714 1 10.5714C0.447715 10.5714 0 10.1237 0 9.57143V3.85714C0 2.83416 0.406376 1.85309 1.12973 1.12973C1.85309 0.406376 2.83416 0 3.85714 0H9.57143C10.1237 0 10.5714 0.447715 10.5714 1C10.5714 1.55228 10.1237 2 9.57143 2H3.85714Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M1 28.5713C1.55228 28.5713 2 29.019 2 29.5713V35.2856C2 35.7781 2.19566 36.2505 2.54394 36.5988C2.89223 36.9471 3.3646 37.1427 3.85714 37.1427H9.57143C10.1237 37.1427 10.5714 37.5905 10.5714 38.1427C10.5714 38.695 10.1237 39.1427 9.57143 39.1427H3.85714C2.83416 39.1427 1.85309 38.7364 1.12973 38.013C0.406377 37.2897 0 36.3086 0 35.2856V29.5713C0 29.019 0.447715 28.5713 1 28.5713Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M7.94506 19.5714C8.09179 19.7679 8.27712 20.0091 8.49806 20.2834C9.12334 21.0596 10.0275 22.0925 11.1431 23.1223C13.4091 25.214 16.3851 27.1429 19.572 27.1429C22.7589 27.1429 25.7348 25.214 28.0008 23.1223C29.1165 22.0925 30.0206 21.0596 30.6459 20.2834C30.8669 20.0091 31.0522 19.7679 31.1989 19.5714C31.0522 19.375 30.8669 19.1337 30.6459 18.8595C30.0206 18.0833 29.1165 17.0503 28.0008 16.0205C25.7348 13.9288 22.7589 12 19.572 12C16.3851 12 13.4091 13.9288 11.1431 16.0205C10.0275 17.0503 9.12334 18.0833 8.49806 18.8595C8.27712 19.1337 8.09179 19.375 7.94506 19.5714ZM32.4291 19.5714C33.2612 19.0167 33.261 19.0165 33.2608 19.0162L33.2589 19.0133L33.2545 19.0067L33.2394 18.9845C33.2266 18.9656 33.2083 18.9389 33.1846 18.9048C33.1372 18.8365 33.0682 18.7387 32.9788 18.6155C32.8 18.3693 32.5387 18.021 32.2034 17.6048C31.5341 16.7739 30.5632 15.6639 29.3574 14.5509C26.9806 12.3569 23.528 10 19.572 10C15.616 10 12.1634 12.3569 9.78656 14.5509C8.58078 15.6639 7.60992 16.7739 6.94055 17.6048C6.60525 18.021 6.34401 18.3693 6.16518 18.6155C6.07572 18.7387 6.00678 18.8365 5.95939 18.9048C5.93569 18.9389 5.91738 18.9656 5.90457 18.9845L5.8895 19.0067L5.8851 19.0133L5.88368 19.0154C5.88348 19.0157 5.88279 19.0167 6.71484 19.5714L5.88279 19.0167C5.65886 19.3526 5.65886 19.7902 5.88279 20.1261L6.71484 19.5714C5.88279 20.1261 5.88259 20.1258 5.88279 20.1261L5.8851 20.1296L5.8895 20.1361L5.90457 20.1584C5.91738 20.1772 5.93569 20.204 5.95939 20.2381C6.00678 20.3063 6.07572 20.4041 6.16518 20.5273C6.34401 20.7736 6.60525 21.1218 6.94055 21.538C7.60992 22.369 8.58078 23.4789 9.78656 24.5919C12.1634 26.786 15.616 29.1429 19.572 29.1429C23.528 29.1429 26.9806 26.786 29.3574 24.5919C30.5632 23.4789 31.5341 22.369 32.2034 21.538C32.5387 21.1218 32.8 20.7736 32.9788 20.5273C33.0682 20.4041 33.1372 20.3063 33.1846 20.2381C33.2083 20.204 33.2266 20.1772 33.2394 20.1584L33.2545 20.1361L33.2589 20.1296L33.2603 20.1275C33.2605 20.1272 33.2612 20.1261 32.4291 19.5714ZM32.4291 19.5714L33.2612 20.1261C33.4851 19.7902 33.4847 19.3521 33.2608 19.0162L32.4291 19.5714Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.573 19.1428C19.3364 19.1428 19.1445 19.3347 19.1445 19.5714C19.1445 19.808 19.3364 19.9999 19.573 19.9999C19.8097 19.9999 20.0016 19.808 20.0016 19.5714C20.0016 19.3347 19.8097 19.1428 19.573 19.1428ZM17.1445 19.5714C17.1445 18.2301 18.2318 17.1428 19.573 17.1428C20.9143 17.1428 22.0016 18.2301 22.0016 19.5714C22.0016 20.9126 20.9143 21.9999 19.573 21.9999C18.2318 21.9999 17.1445 20.9126 17.1445 19.5714Z" fill="#111F61"/>
                        </svg>
                        Our Mission
                    </button>
                    <button class="tab-btn nav-link" data-bs-toggle="tab" data-bs-target="#nav-Value"
                        type="button" role="tab" aria-controls="nav-Value" aria-selected="false" id="nav-Value-tab">
                        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.57414 3.40052C9.58329 3.40027 9.59244 3.40015 9.60159 3.40015H30.4016V4.40015L30.4291 3.40052C31.0655 3.418 31.6888 3.58499 32.2487 3.88799C32.8056 4.18938 33.2842 4.61692 33.6462 5.13636L38.8465 12.3368C39.3614 13.0643 39.6184 13.9429 39.577 14.8332C39.5356 15.7235 39.1981 16.5745 38.6179 17.2511L38.614 17.2557L23.0306 35.2079C22.6728 35.6618 22.2174 36.0296 21.6981 36.2839C21.17 36.5425 20.5897 36.677 20.0016 36.677C19.4136 36.677 18.8333 36.5425 18.3052 36.2839C17.7859 36.0296 17.3305 35.6618 16.9727 35.2079L1.38529 17.2511C0.80515 16.5745 0.467606 15.7235 0.426197 14.8332C0.384788 13.9429 0.6419 13.0643 1.15673 12.3368L1.1623 12.3289L6.35708 5.13622C6.71909 4.61684 7.19764 4.18935 7.75451 3.88799C8.3144 3.58499 8.93775 3.418 9.57414 3.40052ZM30.3866 5.40015H9.61667C9.29829 5.41081 8.98667 5.49526 8.70641 5.64694C8.42251 5.80057 8.17876 6.01886 7.99486 6.28415L7.98369 6.29992L2.78682 13.4956C2.53106 13.8587 2.4034 14.2966 2.42403 14.7403C2.4447 15.1845 2.61281 15.6092 2.90178 15.9471L2.90359 15.9492L18.4997 33.9161C18.5117 33.9299 18.5233 33.944 18.5345 33.9585C18.7081 34.1822 18.9305 34.3632 19.1848 34.4877C19.4391 34.6122 19.7185 34.677 20.0016 34.677C20.2848 34.677 20.5642 34.6122 20.8185 34.4877C21.0727 34.3632 21.2952 34.1822 21.4688 33.9585C21.48 33.944 21.4916 33.9299 21.5036 33.9161L37.0996 15.9492L37.1016 15.947C37.3905 15.609 37.5585 15.1845 37.5792 14.7403C37.5998 14.2967 37.4722 13.8588 37.2165 13.4958L37.2139 13.4921L32.0195 6.29992L32.0084 6.28415C31.8245 6.01886 31.5807 5.80057 31.2968 5.64694C31.0166 5.49526 30.7049 5.41081 30.3866 5.40015Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.0567 3.53154C19.5207 3.83106 19.6541 4.45002 19.3546 4.91403L12.6675 15.2736L20.9241 35.2177C21.1353 35.728 20.8929 36.313 20.3826 36.5242C19.8723 36.7355 19.2874 36.493 19.0762 35.9828L10.619 15.5542C10.4934 15.2508 10.5248 14.9052 10.7028 14.6294L17.6742 3.82937C17.9738 3.36536 18.5927 3.23202 19.0567 3.53154Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M21.0309 3.53028C21.4955 3.23163 22.1142 3.36613 22.4129 3.8307L29.3557 14.6307C29.5334 14.907 29.564 15.253 29.4376 15.5562L20.9233 35.9848C20.7108 36.4945 20.1253 36.7356 19.6156 36.5231C19.1058 36.3106 18.8648 35.7251 19.0772 35.2153L27.3897 15.271L20.7305 4.91222C20.4319 4.44765 20.5664 3.82893 21.0309 3.53028Z" fill="#111F61"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M0.484375 15.1716C0.484375 14.6193 0.93209 14.1716 1.48438 14.1716H38.5129C39.0652 14.1716 39.5129 14.6193 39.5129 15.1716C39.5129 15.7239 39.0652 16.1716 38.5129 16.1716H1.48438C0.93209 16.1716 0.484375 15.7239 0.484375 15.1716Z" fill="#222222"/>
                        </svg>
                        Our Value
                    </button>
                </div>
    
                <div class="tab-content">
                    <div class="tab-pane fade show active" id="nav-Vision" role="tabpanel" aria-labelledby="nav-Vision-tab" >
                        <div class="row">
                            <div class="col-lg-6">
                                <p>
                                    To be the most trusted transformation partner for MSMEs, automotive, and manufacturing enterprises by solving deep-rooted business challenges and driving sustainable, profitable growth. By 2030, we aspire to transform 100 organizations through operational excellence and cultural change.
                                </p>
                                <!-- <ul class="list">
                                    <li>Enable companies to reach global manufacturing standards</li>
                                    <li>Transform 100+ industries by 2030</li>
                                    <li>Build future-ready systems and skilled workforces</li>
                                    <li>Accelerate digital, sustainable growth across the sector</li>
                                </ul> -->
                            </div>
                            <div class="col-lg-6">
                                <img src="/assets/image/vision.webp" class="image w-100 img-fluid" alt="">
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="nav-Mission" role="tabpanel" aria-labelledby="nav-Mission-tab" >
                        <div class="row">
                            <div class="col-lg-6">
                                <p>
                                    “We turn strategy into execution through robust systems, strong leadership, and cultural transformation - delivering measurable impact, industry-ready talent, and sustainable performance for our clients."
                                </p>
                                <!-- <ul class="list">
                                    <li>Industry 4.0 Transformation & Digital Adoption</li>
                                    <li>Digital Quality Systems (DAMS) for robust process control</li>
                                    <li>Developing well-trained engineers into future leaders</li>
                                    <li>ESG-driven operational and cultural enhancement</li>
                                </ul> -->
                            </div>
                            <div class="col-lg-6">
                                <img src="/assets/image/missionImage.webp" class="image w-100 img-fluid" alt="">
                            </div>
                        </div>
                    </div>
                    
                    <div class="tab-pane fade" id="nav-Value" role="tabpanel" aria-labelledby="nav-Value-tab" >
                        <div class="row">
                            <div class="col-lg-6">

                                <ul class="list">
                                    <li><strong>Integrity and Ethics:</strong></li>
                                        Act with honesty and fairness, building trust through strong moral principles.
                                    <li><strong>Customer Centric:</strong></li>
                                        Focus on understanding customer needs and delivering solutions that ensure satisfaction.
                                    <li><strong>Result Oriented:</strong></li>
                                        Drive measurable outcomes efficiently while maintaining quality standards.
                                    <li><strong>People Centric:</strong></li>
                                        Empower and value individuals, fostering collaboration and team success.

                                </ul>
                            </div>
                            <div class="col-lg-6">
                                <img src="/assets/image/valuesImg.webp" class="image w-100 img-fluid" alt="">
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>

        </div>

        <div class="solutionsSec mb-3">
            <div class="row">
                <div class="col-lg-6 py-5 px-3">
                    <div class="solutions">
                        <h4 class="gearIcon2 fw-bold">WHAT WE DO</h4>
                        <h2 class="fw-light">Innovative factory and industry <span class="fw-bold">solutions today</span></h2>
                        <div class="row mt-4">
                            <div class="col-sm-6">
                                <div class="solution">
                                    <img src="/assets/image/Strategic-Planning.png" alt="">
                                    <h5>Strategic Planning</h5>
                                    <p>
                                        Turning vision into action through clear strategy, performance-driven KPIs, and scalable growth.
                                    </p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="solution solution2">
                                    <img src="/assets/image/Operational-Excellence.png" alt="">
                                    <h5>Operational Excellence & Lean Transformation</h5>
                                    <p>
                                        Driving operational excellence by eliminating waste and embedding Lean practices for sustained performance.
                                    </p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="solution solution2">
                                    <img src="/assets/image/Team-Development.png" alt="">
                                    <h5>Digital & Smart Factory Transformation</h5>
                                    <p>
                                        Transforming traditional plants into smart, data-driven factories through digital integration and advanced analytics
                                    </p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="solution">
                                    <img src="/assets/image/Market-Insights.png" alt="">
                                    <h5>Talent Acquisition & Skill Development</h5>
                                    <p>
                                        Building strong organizations through the right hiring and future-ready skill development
                                    </p>
                                </div>
                            </div>
                        </div>
                        <p>Let’s make something great work together. <span class="fw-bold">Get Free Quote</span></p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="solutionsBg">

                        <FloatingDemoWidget/>
                    </div>
                </div>
            </div>
        </div>

        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">MEET THE TEAM</h4>
                    <h2 class="fw-light">Core Team<span class="fw-bold"></span></h2>
                </div>
                <div class="col-sm-0 col-lg-1 px-0"></div>
                <div class="col-sm-12 col-lg-6">
                    <p class="mt-4 pt-2">
                        Our team of seasoned consultant’s leverage deep industry to drive operational excellence and sustainable.
                    </p>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-6 col-lg-4 col-xl-3" v-for="teamMember in teamMembers" :key="teamMember.name">
                    <TeamMemberCard :teamMember="teamMember" @open="openMember" />
                </div>
            </div>
        </div>

        <div class="blueBg py-5">
            <div class="container text-center">
                <h3 class="width-75 text-white px-lg-5 transformTitle">
                    Accelerate Your Growth with Proven Results <br>
                    Trusted by OEMs & Tier-1 Suppliers
                </h3>
                <ul class="checkList">
                    <!-- <li>Stronger operations</li>
                    <li>Better quality & delivery</li>
                    <li>Sustainable performance gains</li> -->
                    <li>Operational Excellence That Delivers Consistent Results</li>
                    <li>Improved Quality, Cost, and Delivery Performance</li>
                    <li>Sustainable, Measurable Business Growth</li>
                </ul>
                <div class="d-flex justify-content-sm-center mt-4">
                    <NuxtLink to="/contact-us" class="arrowBtn">
                        Start Your Transformation
                        <span class="material-symbols-outlined">arrow_forward_ios</span>
                    </NuxtLink>
                </div>

            </div>
        </div>

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
        

        <!-- Team member modal -->
        <div class="modal fade" id="teamMemberModal" tabindex="-1" aria-labelledby="teamMemberModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-header">
                        <!-- <h5 class="modal-title" id="teamMemberModalLabel">{{ modalMember?.name }}</h5> -->
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-4">
                                <div class="imgSec">
                                    <img :src="modalMember?.image" class="teamMemberImg img-fluid" alt="">
                                </div>
                            </div>
                            <div class="col-md-8">
                                <h2 class="mb-3" v-if="modalMember?.bioTitle">{{ modalMember?.bioTitle }}</h2>
                                <h4 class="mb-1">{{ modalMember?.name }}</h4>
                                <h6 class="text-muted mb-3">{{ modalMember?.position }}</h6>
                                <p v-if="modalMember?.bio" class="bio">{{ modalMember.bio }}</p>
                                <p v-else-if="modalMember?.description">{{ modalMember.description }}</p>
                                <!-- <p v-if="modalMember?.contact"><strong>Contact:</strong> <a :href="`tel:${modalMember.contact}`">{{ modalMember.contact }}</a></p> -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <Footer />
    </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
import { useHead } from '#app'
import { faqs } from '~/data/faqs.js';

const modalMember = ref(null);

const openMember = (member) => {
    modalMember.value = member;
    // Use Bootstrap's Modal API
    const modal = new bootstrap.Modal(document.getElementById('teamMemberModal'));
    modal.show();
};

const teamMembers = [
    {
        name: 'T.R Renukanthan',
        position: 'Chief Mentor',
        description: 'Business Excellence – Consultant, DGM Central Quality (Rtd.), Ashok Leyland.',
        bioTitle: 'About Our Mentor',
        bio: `Business Excellence Consultant with 35+ years of experience in manufacturing, quality systems, and operational excellence across automotive and industrial sectors. Former DGM – Central Quality at Ashok Leyland, with deep expertise in TPM, Lean Six Sigma, AIAG Core Tools (PPAP, APQP), and performance management systems. Proven track record in partnering with leadership teams on strategy, KPIs, and shop-floor transformation. Strong focus on process improvement, digital quality adoption, workforce capability building, and sustainable manufacturing excellence. Known for practical, results-driven consulting that delivers measurable improvements in quality, efficiency, and organizational performance.`,
        image: '/assets/image/T.R Renukanthan.png',
    },
    {
        name: 'Ashok Soundararajan',
        position: 'Founder & CEO',
        description: 'Business Consultant.',
        bioTitle: 'About Our Founder',
        bio: `Business Consultant with over a decade of experience in quality engineering, Lean manufacturing, and continuous improvement for manufacturing MSMEs. Currently with Primal Solutions, he has led turnkey quality and profitability improvement projects across automotive and industrial sectors. Strong expertise in Lean Six Sigma, AIAG Core Tools (PPAP, APQP), supplier development, and shop-floor excellence. He has supported OEMs and Tier-1 suppliers including Ashok Leyland, TAFE, and PSA, enabling greenfield setups, process stabilization, and sustainable performance improvement. Known for hands-on execution, structured problem solving, and capability building across engineering teams.`,
        image: '/assets/image/Ashok Soundararajan.webp',
    },
    {
        name: 'Ramkumar S',
        position: 'Senior Consultant',
        description: '',
        bioTitle: '',
        bio: `Senior Consultant with over a decade of experience in quality engineering, Lean manufacturing, and continuous improvement across sheet metal, fabrication, casting, and machining industries. He brings strong expertise in shop-floor training, problem-solving, AIAG Core Tools, and quality management systems. Ramkumar has successfully implemented Lean practices, improved productivity and cost efficiency, and supported vendor development and supply chain performance. He has trained 100+ engineers in core quality tools and problem-solving methodologies. Known for hands-on execution, team building, and practical manufacturing solutions that deliver sustainable operational excellence.`,
        image: '/assets/image/Ramkumar S.png',
    },
    {
        name: 'Sairam D K',
        position: 'Associate Consultant',
        description: '',
        bioTitle: '',
        bio: `Associate Consultant focussed on supporting on-ground implementation and data collection. Trained in core improvement methods and assisting with shop-floor coaching, data analysis and documentation.`,
        image: '/assets/image/Sairam D K.png',
    },
];

const faqsData = ref(faqs);

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.aboutUsBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/aboutUsBnr.png');
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
.numerics{
    margin-left: -20%;
    margin-top: 35px;
    width: 80%;
    text-align: center;
    background-color: #fff;
    border-radius: 30px;
    padding: 40px 20px 5px 20px;
    box-shadow: 14px 17px 150px rgb(149, 164, 181, 0.25);
}
.numerics h3{
    color: #003D33;
    font-weight: 700;
}
.numerics h5{
    color: rgb(17, 31, 97, 0.92);
}

/* Team modal styles */
.modal-header{
    border-bottom: none;
}
.modal-body{
    padding-bottom: 3rem;
}
.imgSec{
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.teamMemberImg{
    width: 80%;
}
.bio{
    font-size: 18px;
}
.numerics .col-4{
    position: relative;
    padding-bottom: 30px;
}
.numerics .col-4::after {
    position: absolute;
    content: "";
    display: block;
    width: 50%;
    left: 25%;
    bottom: 20px;
    height: 5px;
    border-radius: 5px;
    background-color: rgb(159, 182, 178, 0.31);
    margin-top: 20px;
}
.missionSec{
    background-color: #fff;
    border-radius: 40px;
    overflow: hidden;
    margin-top: -25vh; 
    margin-bottom: 6rem;
    box-shadow: 0px 4px 30px rgb(0, 0, 0, 0.1);
}
.missionSec .tab-content{
    padding: 4em 3.4em;
}
.missionSec p{
    color: #81848A;
}
.mission-tabs{
    width: 100%;

}
.mission-tabs button{
    width: 33.33%;
    background-color: #fff;
    color: #222222;
    border-radius: 0;
    border: none;
    padding: 15px 0;
}
.mission-tabs button.active{
    background-color: #111F61;
    color: #fff;
}
.mission-tabs button.active svg path{
    fill: #fff;
}
.mission-tabs button svg{
    width: 30px;
    margin-right: 15px;
}

.missionSec .list li{
    position: relative;
    list-style-type: none;
    line-height: 2.4;
}
.missionSec .list li::before {
    content: '';    
    position: absolute;
    left: -30px;
    top: 50%;
    width: 16px;
    height: 16px;
    transform: translateY(-50%);
    background: url("/assets/image/tickImg.png") no-repeat center;
    background-size: contain;
}
.missionSec .tab-content .image{
    border-radius: 40px;
    aspect-ratio: 492/328;
}
.solutionsSec {
    background-color: #111F61;
    overflow: hidden;
    position: relative;
}
.solutionsSec h2, .solutionsSec h4, .solutionsSec h5 {
    color: #fff;
}
.solutionsSec .solutions {
    color: #fff;
    width: 80%;
    margin: 0 auto;
}

.solutions .solution{
    padding: 1em 1em;
    margin-bottom: 20px;
    border: 1px solid rgb(255, 255, 255, 0.22);
    background-color: transparent;
    border-radius: 30px;
    height: calc(100% - 20px);
}
.solutions .solution img{
    width: 40px;
    height: 40px;
    object-fit: contain;
    margin-bottom: 20px;
}
.solutions .solution2{
    background-color: rgb(255, 255, 255, 0.1);
}
.solution p{
    font-size: 14px;
    margin: 0;
}
.solution h5{
    font-size: 1.15rem;
}
.solutionsBg{
    background-image: url('/assets/image/solutionsBg.webp');
    background-size: cover;
    background-position: center;
    width: 100%;
    height: 100%;
    min-height: 100%;
}
.checkList {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 20px;
    gap: 55px;
    padding: 0;
}
.checkList li{
    position: relative;
    list-style-type: none;
    color: #fff;
    width: 33%;
}
.checkList li::before {
    content: '';    
    position: absolute;
    right: -30px;
    top: 50%;
    width: 1px;
    height: 80%;
    transform: translateY(-50%);
    background: #fff;
    background-size: contain;
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
    .solutionsSec .solutions{
        width: 98%;
    }
}
@media only screen and (max-width:830px) {
    .aboutUsBnr .content h1 {
        font-size: 40px;
    }
    .numerics{
        margin-left: 0%;
        width: 100%;
        padding: 20px 10px 5px;
    }
    .numerics h5{
        font-size: 16px;
    }
    .solutionsBg{
        aspect-ratio: 1/0.8;
        position: relative;
    }
}
@media only screen and (max-width:578px) {
    .mission-tabs button svg{
        display: none;
    }
    .missionSec .tab-content{
        padding: 2em;
    }
    .checkList {
        flex-direction: column;
        gap: 30px;
    }
    .transformTitle{
        text-align: left;
        font-size: 18px;
    }
    .checkList li{
        text-align: left;
        width: 100%;
    }
    .checkList li::before {
        background: transparent;
    }
}
</style>