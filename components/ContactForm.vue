<template>
    <div class="container pb-2">
        <div class="contact-form-row">
            <div class="contact-form-card">
                <h2 class="text-center mb-4">Help Us Knowing What You Need</h2>
                <form>
                    <div class="row gx-3">
                        <div class="col-sm-6 mb-3">
                            <label class="form-label">Name</label>
                            <input type="text" class="form-control" id="contactform-name" placeholder="Jack">
                            <span class="errormsg" id="error-contactform-name"></span>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <label class="form-label">Company Name</label>
                            <input type="text" class="form-control" id="contactform-company" placeholder="Company Name">
                            <span class="errormsg" id="error-contactform-company"></span>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <label class="form-label">E-mail</label>
                            <input type="email" class="form-control" id="contactform-email" placeholder="you@company-email.com">
                            <span class="errormsg" id="error-contactform-email"></span>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <label class="form-label">Contact No</label>
                            <input type="text" class="form-control" id="contactform-phone" placeholder="9099888777">
                            <span class="errormsg" id="error-contactform-phone"></span>
                        </div>
                        <div class="col-12 mb-3">
                            <label class="form-label">Select Service</label>
                            <select class="form-select" id="contactform-service">
                                <option value="">Select a service</option>
                                <option>Operations & Supply Chain Excellence</option>
                                <option>Advanced Automation</option>
                                <option>Process Optimization & Lean</option>
                            </select>
                            <span class="errormsg" id="error-contactform-service"></span>
                        </div>
                        <div class="col-12 mb-4">
                            <label class="form-label">Your needs</label>
                            <textarea class="form-control" id="contactform-needs" rows="4" placeholder="Help us understand what do you need"></textarea>
                            <span class="errormsg" id="error-contactform-needs"></span>
                        </div>
                        <div class="col-12 d-flex justify-content-center">
                            <button type="button" class="btn contact-submit" @click.prevent="submitContactForm">Contact Us Today &nbsp; →</button>
                        </div>
                    </div>
                </form>
                <p class="small text-center mt-4">To learn how Clearbit handles your information,<br> please see our <a href="/privacy-policy">privacy policy</a>.</p>
            </div>
        </div>
    </div>

    <SuccessPopup :show="showSuccess" @close="closeSuccessPopup" />
    <LoadingSpinner :isLoading="isLoading" />

</template>
<script setup>
import { onMounted, ref } from "vue";
import SuccessPopup from './SuccessPopup.vue';
import LoadingSpinner from './LoadingSpinner.vue';

const config = useRuntimeConfig()

// Reactive variables
const isLoading = ref(false);
const showSuccess = ref(false);

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
  const name = document.getElementById('contactform-name').value;
  const company = document.getElementById('contactform-company').value;
  const email = document.getElementById('contactform-email').value;
  const phone = document.getElementById('contactform-phone').value;
  const service = document.getElementById('contactform-service').value;
  const needs = document.getElementById('contactform-needs').value;

  // Validation
  if (name === "") {
    showError('#error-contactform-name', 'Name cannot be blank');
    return;
  }

  if (company === "") {
    showError('#error-contactform-company', 'Company name cannot be blank');
    return;
  }

  if (email === "") {
    showError('#error-contactform-email', 'Email cannot be blank');
    return;
  }

  if (!validateEmail(email)) {
    showError('#error-contactform-email', 'Please enter a valid email address');
    return;
  }

  if (phone === "") {
    showError('#error-contactform-phone', 'Phone number cannot be blank');
    return;
  }

  if (!validatePhone(phone)) {
    showError('#error-contactform-phone', 'Please enter a valid 10-digit phone number');
    return;
  }

  if (service === "") {
    showError('#error-contactform-service', 'Please select a service');
    return;
  }

  if (needs === "") {
    showError('#error-contactform-needs', 'Your needs cannot be blank');
    return;
  }

  // Show loading state
  isLoading.value = true;
  const submitBtn = document.querySelector('.contact-submit');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML = 'Sending...';
  submitBtn.disabled = true;

  const fields = {
    "Name": name,
    "Company Name": company,
    "Email": email,
    "Phone Number": phone,
    "Service": service,
    "Needs": needs
  };

  let emailMsg1 = "Hello Admin,<br><br>";
  emailMsg1 += "A new contact form has been submitted through the ContactForm component on the Primal Solutions website. Please review the details and respond accordingly.<br><br>";
  Object.entries(fields).forEach(([key, value]) => {
    if (value) {
      emailMsg1 += `${key}: ${value}<br/>`;
    }
  });
  emailMsg1 += "<br><br>Best regards,<br>Primal Solutions Website";

  let emailMsg2 = `Hi ${name},<br><br>`;
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
      document.getElementById('contactform-name').value = '';
      document.getElementById('contactform-company').value = '';
      document.getElementById('contactform-email').value = '';
      document.getElementById('contactform-phone').value = '';
      document.getElementById('contactform-service').value = '';
      document.getElementById('contactform-needs').value = '';

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
    showError('#error-contactform-name', 'Failed to submit message. Please try again.');
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
/* Contact form card styles */
.contact-form-row{
    margin-top: -25vh; /* lift card to overlap the background */
    margin-bottom: 6rem;
}
.contact-form-card{
    background: #ffffff;
    color: #111;
    border-radius: 20px;
    padding: 2.5em 5em;
    width: 80%;
    margin: 0 auto;
    box-shadow: 0 -4px 30px rgba(0, 0, 0, 0.04);
    border: 1px solid rgba(6,62,142,0.06);
}
.contact-form-card .form-control, .contact-form-card .form-select{
    border-radius: 8px;
    border: 1px solid #E1E9F0;
    padding: 12px 14px;
}
.contact-form-card .form-label{
    font-size: 0.85rem;
    color: #000;
}
.contact-submit{
    background: #071b6b;
    color: #fff;
    padding: 10px 42px;
    border-radius: 8px;
    border: none;
    width: 70%;
}
.contact-submit:hover{
    background: #0b2a93;
}
.errormsg {
    color: #dc3545;
    font-size: 14px;
    display: none;
    /* margin-top: -20px; */
    /* margin-bottom: 15px; */
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    
}
@media only screen and (max-width:1080px) {
    
}
@media only screen and (max-width:830px) {
    .contact-form-card{
        width: 90%;
        padding: 2rem;
    }
    .contact-form-row{
        margin-top: -25vh;
        margin-bottom: 3rem;
    }
}
@media only screen and (max-width:578px) {
  .contact-submit{
        padding: 10px 30px !important;
    }
    .contact-form-card {
        width: 95%;
        padding: 1.5em;
    }
}
</style>