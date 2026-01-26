<template>

    <Header />

    <div class="policyBnr">
        <div class="container">
            <div class="content text-center">
                <h1 class="fw-light text-white">Privacy <span class="fw-bold">Policy</span></h1>
                <p>
                    Your privacy matters to us. Learn how we protect your information.
                </p>
            </div>
        </div>
    </div>

    <div class="container my-5 py-5">
            <div class="policyWidth">
                <p>
                    This Privacy Policy describes how Primal Solutions ("we," "us," or "our") collects, uses, and protects your personal information when you visit our website or use our services. We are committed to protecting your privacy and ensuring the security of your personal data.
                </p>
                <h6>1. Information We Collect</h6>
                <p>
                    We may collect personal information such as your name, email address, phone number, company information, and other details you provide when contacting us, subscribing to our newsletter, or requesting our services. We also collect non-personal information such as IP addresses, browser types, and usage data through cookies and analytics tools.
                </p>
                <h6>2. How We Use Your Information</h6>
                <p>
                    We use the information we collect to:
                </p>
                <ul>
                    <li>Provide and improve our consulting services</li>
                    <li>Communicate with you about our services and updates</li>
                    <li>Respond to your inquiries and support requests</li>
                    <li>Analyze website usage and improve our content</li>
                    <li>Comply with legal obligations</li>
                </ul>
                <h6>3. Information Sharing</h6>
                <p>
                    We do not sell, trade, or otherwise transfer your personal information to third parties without your consent, except as described in this policy. We may share information with trusted service providers who assist us in operating our website or conducting our business, subject to confidentiality agreements.
                </p>
                <h6>4. Data Security</h6>
                <p>
                    We implement appropriate security measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction. However, no method of transmission over the internet is 100% secure, and we cannot guarantee absolute security.
                </p>
                <h6>5. Cookies and Tracking</h6>
                <p>
                    Our website uses cookies to enhance your browsing experience, analyze site traffic, and personalize content. You can control cookie settings through your browser preferences.
                </p>
                <h6>6. Your Rights</h6>
                <p>
                    You have the right to access, update, or delete your personal information. You may also opt out of marketing communications at any time. To exercise these rights, please contact us using the information provided below.
                </p>
                <h6>7. Third-Party Links</h6>
                <p>
                    Our website may contain links to third-party websites. We are not responsible for the privacy practices or content of these external sites. We encourage you to review their privacy policies.
                </p>
                <h6>8. Changes to This Policy</h6>
                <p>
                    We may update this Privacy Policy from time to time. Any changes will be posted on this page with an updated effective date. Your continued use of our website after changes are made constitutes acceptance of the revised policy.
                </p>
                <h6>9. Contact Us</h6>
                <p>
                    If you have any questions about this Privacy Policy or our data practices, please contact us at:
                    <br>
                </p>
                <h6>Primal Solutions</h6>
                <p>Email: <a href="mailto:info@primalsolutions.com">info@primalsolutions.com</a></p>
                <p>Phone: <a href="tel: +91 00000 00000">+91 00000 00000</a></p>

            </div>
        </div>

        <Footer />
    

</template>
<script setup>

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
