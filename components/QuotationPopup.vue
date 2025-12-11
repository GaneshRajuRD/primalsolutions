<template>
    <div>
        <LoadingSpinner :isLoading="showSuccessLoader" />
        <SuccessPopup :show="showSuccess" @close="closeSuccessPopup" />
        <div class="modal fade" id="QuotationPopup">
            <div class="modal-dialog modal-dialog-centered modal-xl">
                <div class="modal-content form-modal">

                    <img loading="lazy" src="/assets/image/ceo-portrait.webp" class="ceo-portrait img-fluid" />
                    <img loading="lazy" src="/assets/image/registerPopupVector.png" class="quotationPopupVector img-fluid" />

                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    <!-- Modal Header -->
                    <div class="modal-header border-0 justify-content-center">

                    </div>
                    <!-- Modal body -->
                    <div class="modal-body">
                        <div class="row mt-3">
                            <div class="col-lg-6">
                                <img loading="lazy" src="/assets/image/ceo-portrait.webp" class="d-block d-lg-none img-fluid w-100" />
                            </div>
                            <div class="col-lg-6 mt-4 mt-lg-0">
                                <div class="quotationForm">
                                    <h5 class="text-center fw-bold lightblack-text">Get a Quote</h5>
                                    <p class="text-center grey-text">
                                        You are one step closer to streamlining your operations and digitising your practice.
                                    </p>

                                    <form class="form" @submit.prevent="submitQuotationForm">
                                    <div class="form-group">
                                        <input type="text" class="form-control mt-2" placeholder="Enter your name" id="quotation-name" v-model="quotationForm.name">
                                        <span class="errormsg" id="err-quotation-name"></span>
                                    </div>
                                    <div class="form-group">
                                        <input type="text" class="form-control mt-2" placeholder="Position or designation" id="quotation-Position" v-model="quotationForm.position">
                                        <span class="errormsg" id="err-quotation-Position"></span>
                                    </div>
                                    <div class="form-group">
                                        <input type="text" class="form-control mt-2" placeholder="Organization name" id="quotation-organization" v-model="quotationForm.organization">
                                        <span class="errormsg" id="err-quotation-organization"></span>
                                    </div>
                                    <div class="form-group">
                                        <input type="text" class="form-control mt-2" placeholder="Enter Your Phone Number" id="quotation-phone" v-model="quotationForm.phone">
                                        <span class="errormsg" id="err-quotation-phone"></span>
                                    </div>
                                    <div class="form-group">
                                        <input type="email" class="form-control mt-2" placeholder="Email Id" id="quotation-email" v-model="quotationForm.email">
                                        <span class="errormsg" id="err-quotation-email"></span>
                                    </div>
                                        <div class="row mt-4">
                                            <div class="col-sm-12 d-flex justify-content-center">
                                                <button class="submit" type="submit">Schedule a call</button>
                                            </div>
                                        </div>
                                    </form>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { ref } from 'vue'
import LoadingSpinner from './LoadingSpinner.vue'
import SuccessPopup from './SuccessPopup.vue'

const config = useRuntimeConfig()

const isLoading = ref(false)
const showSuccess = ref(false)
const showSuccessLoader = ref(false)

// Quotation form data
const quotationForm = ref({
  name: '',
  position: '',
  organization: '',
  phone: '',
  email: ''
})

const showError = (selector, message) => {
  const errorElement = document.querySelector(selector)
  if (errorElement) {
    errorElement.textContent = message
    errorElement.style.display = 'block'
    setTimeout(() => {
      errorElement.style.display = 'none'
    }, 5000)
  }
}

const validateEmail = (email) => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
  return emailRegex.test(email)
}

const validatePhone = (phone) => {
  const phoneRegex = /^[0-9]{10}$/
  return phoneRegex.test(phone.replace(/\s+/g, ''))
}

const submitQuotationForm = async () => {
  // Clear all previous errors
  document.querySelectorAll('.errormsg').forEach(el => el.style.display = 'none')

  // Validation
  if (quotationForm.value.name === "") {
    showError('#err-quotation-name', 'Name cannot be blank')
    return
  }

  if (quotationForm.value.position === "") {
    showError('#err-quotation-Position', 'Position cannot be blank')
    return
  }

  if (quotationForm.value.organization === "") {
    showError('#err-quotation-organization', 'Organization cannot be blank')
    return
  }

  if (quotationForm.value.phone === "") {
    showError('#err-quotation-phone', 'Phone number cannot be blank')
    return
  }

  if (!validatePhone(quotationForm.value.phone)) {
    showError('#err-quotation-phone', 'Please enter a valid 10-digit phone number')
    return
  }

  if (quotationForm.value.email === "") {
    showError('#err-quotation-email', 'Email cannot be blank')
    return
  }

  if (!validateEmail(quotationForm.value.email)) {
    showError('#err-quotation-email', 'Please enter a valid email address')
    return
  }

  // Show success loader immediately after validation
  showSuccessLoader.value = true

  const fields = {
    "Name": quotationForm.value.name,
    "Position": quotationForm.value.position,
    "Organization": quotationForm.value.organization,
    "Phone Number": quotationForm.value.phone,
    "Email": quotationForm.value.email
  }

  let emailMsg1 = "Hello Admin,<br><br>"
                + "A new registration has been submitted through the Quotation Popup on the Primal Solutions website. Please review the details and respond accordingly.<br><br>"
  Object.entries(fields).forEach(([key, value]) => {
    if (value) {
      emailMsg1 += `${key}: ${value} <br/>`
    }
  })

  emailMsg1 = emailMsg1 + "<br>"
            + "<br/>Best regards,<br>"
            + "Primal Solutions Website";

  let emailMsg2 = "Hi " + quotationForm.value.name
  emailMsg2 = emailMsg2 + "<br><br>"
            + "Thank You for contacting with Primal Solutions! 🏥<br><br>"
            + "Your registration has been successfully received. Our team will review your details and get back to you as soon as possible. We appreciate your interest in our services.<br><br>"
            + "For any urgent queries, feel free to contact us directly. We look forward to serving you!<br><br>"
            + "Best regards,<br>"
            + "Primal Solutions Team<br>"

  const emailData = {
    adminEmail: {
      to: "ganeshraju@mocerohealth.in",
      cc: "ganeshraju@mocerohealth.in",
      subject: "Website Registration Form - Primal Solutions",
      html: emailMsg1
    },
    userEmail: {
      to: quotationForm.value.email,
      cc: quotationForm.value.email,
      subject: "Thank you for contacting with Primal Solutions",
      html: emailMsg2
    }
  }

  try {
    const response = await fetch(config.public.emailApi, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(emailData)
    })

    const data = await response.json()

    if (data.status === true) {
      quotationForm.value = {
        name: '',
        position: '',
        organization: '',
        phone: '',
        email: ''
      }

      // After 2 seconds, hide loader and show success popup
      setTimeout(() => {
        showSuccessLoader.value = false
        showSuccess.value = true
      }, 2000)
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    showSuccessLoader.value = false
  }

}

// Close success popup function
const closeSuccessPopup = () => {
  showSuccess.value = false
  // Close the modal
  const modal = document.getElementById('QuotationPopup')
  if (modal) {
    const bsModal = bootstrap.Modal.getInstance(modal)
    if (bsModal) {
      bsModal.hide()
    }
  }
}

</script>
<style scoped>
.loginBtn{
    color: #3B9DD5;
    text-decoration: none;
}
.quotationForm{
    position: relative;
    z-index: 4;
}
.quotationForm .mail{
    color: #435a47;
    text-decoration: none;
}
.quotationForm input,.quotationForm select{
  border: 1px solid #E1E1E1;
  color: #444;
  border-radius: 50px;
  margin-bottom: 20px;
  padding: 10px 20px;
  background-color: #fff;
}
.quotationForm .submit{
  background-color: #111F61;
  color: #fff;
  border-radius: 30px;
  width: 100%;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  border: none;
}
#QuotationPopup .modal-dialog{
  transition: 0.7s;
}
#QuotationPopup .modal-header{
  padding: 0;
}
#QuotationPopup .form-modal{
  padding: 25px;
  border-radius: 0px;
}
.query{
    height: 90px;
}

#QuotationPopup .modal-content {
    border-radius: 25px;
    position: relative;
    padding: 4% 10%;
}
#QuotationPopup .modal-body {
    background-image: linear-gradient(-31deg, #F8F8F8 0%, #F6EEFF 100%);
    border-radius: 28px;
    padding: 4%;
    
}
#QuotationPopup .modal-content .btn-close{
    position: absolute;
    right: 24px;
    top: 24px;
    z-index: 10;
    background-image: url(/assets/image/closeImg.png);
    background-position: center;
    background-size: 20px, contain;
    background-repeat: no-repeat;
    opacity: 1;
    width: 20px;
    height: 20px;
}
.ceo-portrait{
    width: 40%;
    height: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 6%;
    object-fit: contain;
    object-position: left bottom;
    z-index: 3;
}
.quotationPopupVector{
    width: 92%;
    height: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0%;
    object-fit: contain;
    object-position: left bottom;
    z-index: 2;
}
.errormsg{
    color: red;
    font-size: 12px;
    display: none;
}
@media only screen and (max-width: 830px){
    .ceo-portrait{
        display: none;
    }
}

</style>