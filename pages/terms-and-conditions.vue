<template>
    <div>
        <Header />

        <div class="policyBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-light text-white">Terms & <span class="fw-bold">Conditions</span></h1>
                    <p>
                        Understand the rules and guidelines for using our services.
                    </p>
                </div>
            </div>
        </div>

        <div class="container my-5 py-5">
            <div class="policyWidth">
                <p>
                    These Terms and Conditions ("Terms") govern your use of the Primal Solutions website and services. By accessing or using our website and services, you agree to be bound by these Terms. If you do not agree to these Terms, please do not use our website or services.
                </p>
                <h6>1. Services</h6>
                <p>
                    Primal Solutions provides consulting services in industrial innovation, process optimization, automation, and business strategy for manufacturing companies, OEMs, and Tier-1 suppliers. Our services include but are not limited to strategic planning, operational excellence, team development, and market insights.
                </p>
                <h6>2. User Responsibilities</h6>
                <p>
                    You agree to:
                </p>
                <ul>
                    <li>Provide accurate and complete information when requesting our services</li>
                    <li>Use our website and services only for lawful purposes</li>
                    <li>Not interfere with the proper functioning of our website</li>
                    <li>Respect intellectual property rights</li>
                </ul>
                <h6>3. Intellectual Property</h6>
                <p>
                    All content on our website, including text, graphics, logos, and software, is the property of Primal Solutions or its licensors and is protected by copyright and other intellectual property laws. You may not reproduce, distribute, or create derivative works without our written permission.
                </p>
                <h6>4. Confidentiality</h6>
                <p>
                    We respect the confidentiality of information you provide. We may be required to share proprietary information with our clients as part of our consulting services. We maintain strict confidentiality agreements with our clients and team members.
                </p>
                <h6>5. Limitation of Liability</h6>
                <p>
                    To the fullest extent permitted by law, Primal Solutions shall not be liable for any indirect, incidental, special, or consequential damages arising out of or in connection with your use of our website or services.
                </p>
                <h6>6. Indemnification</h6>
                <p>
                    You agree to indemnify and hold Primal Solutions harmless from any claims, damages, or expenses arising from your use of our website or services, or your violation of these Terms.
                </p>
                <h6>7. Termination</h6>
                <p>
                    We reserve the right to terminate or suspend your access to our website and services at any time, without notice, for any reason.
                </p>
                <h6>8. Governing Law</h6>
                <p>
                    These Terms shall be governed by and construed in accordance with the laws of India, without regard to its conflict of law provisions.
                </p>
                <h6>9. Changes to Terms</h6>
                <p>
                    We may update these Terms from time to time. Any changes will be posted on this page with an updated effective date. Your continued use of our website and services after changes are made constitutes acceptance of the revised Terms.
                </p>
                <h6>10. Contact Us</h6>
                <p>
                    If you have any questions about these Terms, please contact us at:
                    <br>
                </p>
                <h6>Primal Solutions</h6>
                <p>Email: <a href="mailto:info@primalsolutions.com">info@primalsolutions.com</a></p>
                <p>Phone: <a href="tel: +91 00000 00000">+91 00000 00000</a></p>
            </div>
        </div>

        <Footer />

    </div>
</template>
<script setup>
import { onMounted } from "vue";

</script>
<style scoped>
.policyBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/aboutUsBnr.webp');
    height: 90vh;
    display: flex;
    align-items: center;
    text-align: center;
    color: #fff;
}
.policyBnr .content {
    height: 100%;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}

.policyBnr .content h1 {
    font-size: 60px;
}

.policyWidth{
    width: 90%;
    margin: 0 auto;
}

@media only screen and (max-width:1440px) {

}
@media only screen and (max-width:1280px) {
    .policyBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .policyBnr .content h1 {
        font-size: 44px;
    }
}
@media only screen and (max-width:830px) {
    .policyBnr .content h1 {
        font-size: 40px;
    }

}
@media only screen and (max-width:578px) {

}
</style>
