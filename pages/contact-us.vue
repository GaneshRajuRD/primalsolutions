<template>
    <div class="body">
        <Header />

        <div class="contactBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-bold">Contact Us</h1>
                    <p>
                        Explore exciting opportunities and grow your career in property management with us
                    </p>
                </div>
            </div>
        </div>

        <div class="container py-5">
            <div class="row">
                <div class="col-sm-12 col-lg-5">
                    <h4 class="gearIcon fw-bold">CONTACT US</h4>
                    <h2 class="fw-light">Get in touch <span class="fw-bold">with us</span></h2>
                    <p class="greyText">
                        Reach out for any inquiries, support, or to discuss how we can meet your industrial needs.
                    </p>
                </div>
            </div>

            <div class="formSec mt-4">
                <div class="row">
                    <div class="col-lg-8 px-sm-0">
                        <div class="contact-card">
                            <form>
                                <div class="row gx-3">
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">First Name</label>
                                        <input type="text" class="form-control" id="contact-firstname" placeholder="Enter First Name">
                                        <span class="errormsg" id="error-contact-firstname"></span>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Last Name</label>
                                        <input type="text" class="form-control" id="contact-lastname" placeholder="Enter Last Name">
                                        <span class="errormsg" id="error-contact-lastname"></span>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Email</label>
                                        <input type="email" class="form-control" id="contact-email" placeholder="Enter your Email">
                                        <span class="errormsg" id="error-contact-email"></span>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Phone</label>
                                        <input type="text" class="form-control" id="contact-phone" placeholder="Enter Phone Number">
                                        <span class="errormsg" id="error-contact-phone"></span>
                                    </div>

                                    <div class="col-12 mb-3">
                                        <label class="form-label">Select Your Sector</label>
                                        <select class="form-control" id="contact-sector">
                                            <option value="">Select a Sector</option>
                                            <option v-for="sector in sectors" :key="sector" :value="sector">{{ sector }}</option>
                                        </select>
                                        <span class="errormsg" id="error-contact-sector"></span>
                                    </div>

                                    <div class="col-12 mb-3">
                                        <label class="form-label">Service Required</label>
                                        <select class="form-control" id="contact-service">
                                            <option value="">Select a Service</option>
                                            <option v-for="service in services" :key="service" :value="service">{{ service }}</option>
                                        </select>
                                        <span class="errormsg" id="error-contact-service"></span>
                                    </div>

                                    <div class="col-12 mb-4">
                                        <label class="form-label">Message</label>
                                        <textarea class="form-control" id="contact-message" rows="6" placeholder="Enter your Message here..."></textarea>
                                        <span class="errormsg" id="error-contact-message"></span>
                                    </div>

                                    <div class="col-12 d-flex justify-content-center">
                                        <button type="button" class="btn sendBtn" @click.prevent="submitContactForm">Send Your Message</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-4 px-sm-0">
                        <div class="info-cards">
                            <div class="info-card">
                                <img src="/assets/image/mailIcon2.png" class="icon" alt="">
                                <div class="text">support@skillbridge.com</div>
                            </div>
                            <div class="info-card">
                                <img src="/assets/image/callIcon2.png" class="icon" alt="">
                                <div class="text">+91 00000 00000</div>
                            </div>
                            <div class="info-card">
                                <img src="/assets/image/locationIcon.png" class="icon" alt="">
                                <div class="text">Some Where in the World</div>
                            </div>
                            <div class="info-card social">
                                <div class="icons">
                                    <img src="/assets/image/fbIcon2.png" class="icon" alt="">
                                    <img src="/assets/image/twitterIcon2.png" class="icon" alt="">
                                    <img src="/assets/image/linkedInIcon2.png" class="icon" alt="">
                                </div>
                                <div class="text">Social Profiles</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div class="container pt-4 pb-5">
            <div class="mapSec">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10997.205840495131!2d80.24203990732217!3d12.965490158726038!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525d6d9e5f8f2b%3A0x7afb2aa6caf3f8e1!2sFreshworks!5e0!3m2!1sen!2sin!4v1764143471688!5m2!1sen!2sin" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>

        <SuccessPopup :show="showSuccess" @close="closeSuccessPopup" />
        <LoadingSpinner :isLoading="isLoading" />

        <Footer />

        
    </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
import SuccessPopup from '../components/SuccessPopup.vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';

const config = useRuntimeConfig()

// Reactive variables
const isLoading = ref(false);
const showSuccess = ref(false);

// Sectors and Services data
const sectors = ref([
    'Automotive Manufacturing',
    'Agricultural & Farm Equipment',
    'Elevators & Construction Equipment',
    'Off-Road & Earthmoving Industry',
    'FMCG Manufacturing',
    'Electronics Production'
]);

const services = ref([
    'Business Strategy',
    'Business Transformation',
    'Market Research',
    'Operations Supply Chain Excellence',
    'Skill Development Programs',
    'Talent Hiring Management'
]);

// Validation functions
const validateEmail = (email) => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
};

const validatePhone = (phone) => {
  const phoneRegex = /^[0-9]{10}$/;
  return phoneRegex.test(phone.replace(/\s+/g, ''));
};

const showError = (selector, message) => {
  const errorElement = document.querySelector(selector);
  if (errorElement) {
    errorElement.textContent = message;
    errorElement.style.display = 'block';
    setTimeout(() => {
      errorElement.style.display = 'none';
    }, 5000);
  }
};

// Form submission function
const submitContactForm = async () => {
  // Clear all previous errors
  document.querySelectorAll('.errormsg').forEach(el => el.style.display = 'none');

  // Get form values
  const firstName = document.getElementById('contact-firstname').value;
  const lastName = document.getElementById('contact-lastname').value;
  const email = document.getElementById('contact-email').value;
  const phone = document.getElementById('contact-phone').value;
  const sector = document.getElementById('contact-sector').value;
  const service = document.getElementById('contact-service').value;
  const message = document.getElementById('contact-message').value;

  // Validation
  if (firstName === "") {
    showError('#error-contact-firstname', 'First name cannot be blank');
    return;
  }

  if (lastName === "") {
    showError('#error-contact-lastname', 'Last name cannot be blank');
    return;
  }

  if (email === "") {
    showError('#error-contact-email', 'Email cannot be blank');
    return;
  }

  if (!validateEmail(email)) {
    showError('#error-contact-email', 'Please enter a valid email address');
    return;
  }

  if (phone === "") {
    showError('#error-contact-phone', 'Phone number cannot be blank');
    return;
  }

  if (!validatePhone(phone)) {
    showError('#error-contact-phone', 'Please enter a valid 10-digit phone number');
    return;
  }

  if (sector === "") {
    showError('#error-contact-sector', 'Sector cannot be blank');
    return;
  }

  if (service === "") {
    showError('#error-contact-service', 'Service required cannot be blank');
    return;
  }

  if (message === "") {
    showError('#error-contact-message', 'Message cannot be blank');
    return;
  }

  // Show loading state
  isLoading.value = true;
  const submitBtn = document.querySelector('.sendBtn');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML = 'Sending...';
  submitBtn.disabled = true;

  const fields = {
    "First Name": firstName,
    "Last Name": lastName,
    "Email": email,
    "Phone Number": phone,
    "Sector": sector,
    "Service Required": service,
    "Message": message
  };

  let emailMsg1 = "Hello Admin,<br><br>";
  emailMsg1 += "A new contact form has been submitted through the Contact Us page on the Primal Solutions website. Please review the details and respond accordingly.<br><br>";
  Object.entries(fields).forEach(([key, value]) => {
    if (value) {
      emailMsg1 += `${key}: ${value}<br/>`;
    }
  });
  emailMsg1 += "<br><br>Best regards,<br>Primal Solutions Website";

  let emailMsg2 = `Hi ${firstName},<br><br>`;
  emailMsg2 += "Thank you for contacting Primal Solutions! 🏥<br><br>";
  emailMsg2 += "We have received your message and our team will get back to you as soon as possible. We appreciate your interest in our services.<br><br>";
  emailMsg2 += "For any urgent queries, feel free to contact us directly. We look forward to assisting you!<br><br>";
  emailMsg2 += "Best regards,<br>Primal Solutions Team<br>";

  const emailData = {
    adminEmail: {
      to: "ganeshraju@mocerohealth.in",
      cc: "ganeshraju@mocerohealth.in",
      subject: "Contact Form - Primal Solutions",
      html: emailMsg1
    },
    userEmail: {
      to: email,
      cc: email,
      subject: "Thank you for contacting Primal Solutions",
      html: emailMsg2
    }
  };

  try {
    const response = await fetch(config.public.emailApi, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(emailData)
    });

    const data = await response.json();

    if (data.status === true) {
      // Clear form
      document.getElementById('contact-firstname').value = '';
      document.getElementById('contact-lastname').value = '';
      document.getElementById('contact-email').value = '';
      document.getElementById('contact-phone').value = '';
      document.getElementById('contact-sector').value = '';
      document.getElementById('contact-service').value = '';
      document.getElementById('contact-message').value = '';

      // Reset button
      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
      isLoading.value = false;

      // Show success popup
      showSuccess.value = true;
    } else {
      throw new Error('Failed to send emails');
    }
  } catch (error) {
    console.error('Error submitting form:', error);
    showError('#error-contact-firstname', 'Failed to submit message. Please try again.');
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;
    isLoading.value = false;
  }
};

// Close success popup function
const closeSuccessPopup = () => {
  showSuccess.value = false;
};

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.contactBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/contactBnr.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
.contactBnr h1{
    color: #fff;
}
.contactBnr .content {
    height: 90vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}
.contactBnr .content h1 {
    font-size: 60px;
}

.formSec{
    background: #fff;
    /* padding: 3em; */
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(2,6,23,0.06);
    border: 1px solid rgba(6,62,142,0.04);
}
.formSec input, .formSec textarea ,.formSec select{
    background-color: #FCFCFD;
    border: 1px solid #F1F1F3;
    border-radius: 6px;
    padding: 10px 20px;
}
.contact-card{
    padding: 3em;
    /* border-right: 1px solid #F1F1F3; */
}
.contact-card .form-label{
    font-size: 0.9rem;
    color: #262626;
    margin-bottom: 8px;
    font-weight: 500;
}
.sendBtn{
    background: #071b6b;
    color: #fff;
    padding: 10px 26px;
    border-radius: 8px;
    border: none;
}
.errormsg {
    color: #dc3545;
    font-size: 14px;
    display: none;
    /* margin-top: -20px; */
    /* margin-bottom: 15px; */
}
.info-cards{
    display: flex;
    flex-direction: column;
    gap: 2em;
    padding: 3em;
    border-left: 1px solid #F1F1F3;
}
.info-card{
    padding: 2em;
    text-align: center;
    background-color: #FCFCFD;
    border: 1px solid #F1F1F3;
    border-radius: 10px;
}
.info-card .icon{
    width: 42px;
    height: 42px;
    padding: 10px;
    background-color: #F7F7F8;
    border: 1px solid #F1F1F3;
    border-radius: 8px;
    margin-bottom: 15px;
}
.info-card .text{
    color: #333;
}
.info-card.social .icons{
    display:flex;
    justify-content: center;
    gap:12px;
    margin-right:12px;
}
.socialIcon{
    width:34px;
    height:34px;
    background:#f0f0f0;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    border-radius:6px;
}
.mapSec{
    height: 450px;
}
.mapSec iframe{
    width: 100%;
    height: 100%;
    border-radius: 8px;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    .contactBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .contactBnr .content h1 {
        font-size: 44px;
    }
}
@media only screen and (max-width:830px) {
    .contactBnr .content h1 {
        font-size: 40px;
    }
}
@media only screen and (max-width:578px) {
    
}
</style>