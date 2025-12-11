<template>


        <div class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-xl-6 col-lg-12">
                        <img src="/assets/image/primalLogo.png" class="footerLogo img-fluid" alt="">
                        <div class="row">
                            <div class="col-sm-5">
                                <h5 class="line-height-15 mb-4">1498w Fluton ste, STE <br>2D Chicgo, IL 63867.</h5>
                                <a class="d-inline-block mb-4" href="mailto: info@seafarers.io ">info@seafarers.io </a><br>
                                <a class="d-inline-block mb-2" href="tel: (123) 456789000">(123) 456789000</a>

                                <div class="socialLinks">
                                    <a href="#"><img src="/assets/image/twitterIcon.svg" alt=""></a>
                                    <a href="#"><img src="/assets/image/fbIcon.svg" alt=""></a>
                                    <a href="#"><img src="/assets/image/ytIcon.svg" alt=""></a>
                                    <a href="#"><img src="/assets/image/instaIcon.svg" alt=""></a>
                                </div>
                            </div>
                            <div class="col-sm-1 px-0"></div>
                            <div class="col-sm-5 px-sm-0">
                                <img src="/assets/image/footerImg.webp" class="img-fluid mb-4" />
                                <NuxtLink class="callBtn" to="/contact-us" type="" data-bs-toggle="modal" data-bs-target="#QuotationPopup">Schedule a 10 minute call
                                    <span></span>
                                </NuxtLink>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-6 col-lg-12 mt-5 mt-xl-0">
                        <h2 class="Adlinnaka mb-4"><span class="yellowText">Let`s</span> start with us in shaping your <span class="yellowText">business growth</span></h2>
                        <div class="row">
                            <div class="col-sm-4 col-xl-3 col-xxl-4">
                                <h5 class="mb-4">Site Map</h5>
                                <ul>
                                    <li><NuxtLink to="/">Home</NuxtLink></li>
                                    <li><NuxtLink to="/about-us">About Us</NuxtLink></li>
                                    <li><NuxtLink to="/sectors">Sectors</NuxtLink></li>
                                    <li><NuxtLink to="/careers">Careers</NuxtLink></li>
                                    <li><NuxtLink to="/contact-us">Contact Us</NuxtLink></li>
                                </ul>

                            </div>
                            <div class="col-sm-4 col-xl-4 col-xxl-4">
                                <h5 class="mb-4">Resources</h5>
                                <ul>
                                    <li><NuxtLink to="/resources#CaseStudies">Case Studies</NuxtLink></li>
                                    <li><NuxtLink to="/resources#Blogs">Blogs</NuxtLink></li>
                                    <li><NuxtLink to="/resources#Gallery">Gallery</NuxtLink></li>
                                </ul>
                            </div>
                            <div class="col-sm-5">
                                <h5 class="mb-4">Services</h5>
                                <ul>
                                    <li><NuxtLink to="/services/business-strategy">Business Strategy</NuxtLink></li>
                                    <li><NuxtLink to="/services/business-transformation">Business Transformation</NuxtLink></li>
                                    <li><NuxtLink to="/services/skill-development-programs">Skill Development Programs</NuxtLink></li>
                                    <li><NuxtLink to="/services/operations-supply-chain-excellence">Operations & Supply Chain Excellence</NuxtLink></li>
                                    <li><NuxtLink to="/services/talent-hiring-management">Talent Hiring & Management</NuxtLink></li>
                                    <li><NuxtLink to="/services/market-research">Market Research</NuxtLink></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row pt-4 mt-sm-5 mt-4 footerBottomSec">
                    <div class="col-lg-6 copyrightSec">
                        <p>Copyright © 2025, PRIMAL SOLUTIONS. All rights reserved.</p>
                    </div>
                    <div class="col-lg-6">
                        <div class="policySec">
                            <NuxtLink to="/privacy-policy">Privacy policy</NuxtLink>
                            <NuxtLink to="/terms-and-conditions" class="border-0">Terms & Conditions</NuxtLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <QuotationPopup />


</template>

<script setup>
import { onMounted } from "vue";

</script>
<style scoped>
.footer{
    background-image: url(/assets/image/footerVector.png),linear-gradient(-60deg,#132162,#132162);
    background-repeat: no-repeat;
    background-size: 35%, contain;
    background-position: right bottom;
    background-blend-mode: overlay;
    padding: 50px 0 10px;
    color: #fff;
}
.footer .footerLogo{
    height: 100px;
    width: 100%;
    object-fit: contain;
    max-width: 350px;
    margin-bottom: 15px;
}
.footer a{
    color: #fff;
    text-decoration: none;
}
.footer h5{
    color: #fff;
}
.footer h2{
    color: #fff;
}
.footerBottomSec{
    border-top: 1px solid rgba(255, 255, 255, 0.4);
}
.footer .callBtn{
    padding: 10px 15px;
    border: 1px solid #fff;
    border-radius: 30px;
    position: relative;
}
.footer .callBtn span{
    display: inline-block;
    height: 12px;
    width: 12px;
    background-color: #00E0AF;
    border-radius: 50%;
    margin-left: 5px;
}
.footer ul{
    padding: 0;
    list-style-type: none;
}
.footer ul li{
    margin-bottom: 14px;
    line-height: 1.2;
}
.footer ul li a{
    color: rgb(255, 255, 255, 0.5);
}
.footer ul li a:hover{
    transition: 0.4s;
    color: rgb(255, 255, 255, 1);
}

.footer .footerList{
    list-style-type: disc;
    padding-left: 1.2rem;
}
.footer .sublink{
    color: #fff;
}
.policySec{
    text-align: end;
}
.policySec a{
    padding: 0 10px;
    border-right: 1px solid #fff;
}
.footerContact{
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translate(-50%);
    z-index: 1;
    /* background-color: #00E0AF; */
    background-color: #01d2a4;
    color: #fff;
    padding: 5px 12px;
    border-radius: 30px;
    opacity: 0;
}
.footer:hover .footerContact{
    opacity: 1;
    transition: 0.6s;
}
.socialLinks{
    margin-top: 30px;
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}
.socialLinks a{
    height: 40px;
    width: 40px;
    padding: 8px;
    text-decoration: none;
    border: 1px solid rgb(255, 255, 255, 0.2);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.socialLinks a img{
    width: 20px;
    height: 20px;
}
.socialLinks a:hover{
    transition: 0.4s;
    border: 1px solid rgb(255, 255, 255, 0.8);
}

@media only screen and (max-width:1440px){
    
}
@media only screen and (max-width:1280px){
    .footer{
        background-size: 45%, contain;
    }
    
}

@media only screen and (max-width:1025px){
    /* .footerContact{
        top: 10%;
    } */
}
@media only screen and (max-width:830px){
    .policySec, .copyrightSec{
        text-align: center;
    }
    .footer{
        background-size: 55%, contain;
    }
    
}
@media only screen and (max-width:578px){
    .footer{
        background-size: 85%, contain;
    }
}
@media only screen and (min-width:1400px){
    
}
</style>