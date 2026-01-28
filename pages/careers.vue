<template>
    <div class="body">
        <Header />
        <Loader />

        <div class="careersBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-bold">Careers</h1>
                    <p>
                        Explore exciting opportunities and grow your career in property management with us
                    </p>
                </div>
            </div>
        </div>

        <div class="container py-5">
            <div class="whyUsCard">
                <div class="row">
                    <div class="col-lg-5">
                        <img src="/assets/image/careersImg.webp" class="mb-4 mb-lg-0 w-100 img-fluid" alt="">
                    </div>
                    <div class="col-lg-7">
                        <div class="ps-lg-3">
                            <h2 class="bigFont">Why should you consider joining us</h2>
                            <h3 class="fw-light">
                                “We build an environment that supports your goals, respects your space, and helps you grow at a pace that keeps your work and personal life in harmony.
                            </h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container">
            <h4 class="mb-4 mt-3">Positions Available</h4>

            <div class="careerCard" v-for="career in careers" :key="career.title">
                <div class="d-flex flex-column flex-lg-row justify-content-between">
                    <div>
                        <h5>{{ career.title }}</h5>
                    </div>
                    <div>
                        <p>{{ career.experience }}</p>
                    </div>
                </div>
                <span>{{ career.qualification }}</span>
                <p class="my-4 py-3">
                    {{ career.description }}
                </p>
                <div class="applySection">
                    <div>
                        <span>No of positions: </span>
                        <span class="text-black">{{ career.positions }}</span>
                        <span class="careerDate">{{ career.date }}</span>
                    </div>
                    <div class="mt-sm-0 mt-3 text-end">
                        <button href="#" class="applyBtn" @click="applyForCareer(career)">Apply</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="blueBg pt-5">
            <div class="container">
                <div class="row formSec">
                    <div class="col-lg-6 text-white">
                        <div class="h-100 d-flex flex-column justify-content-between">
                            <div>
                                <h1 class="text-white width-75 fw-bold mx-0">Let's Build Your Career with Us</h1>
                                <p class="width-75 mx-0 mt-3">
                                    Join Scarfree Centre and take the next step in your career with a team dedicated to excellence in healthcare. We offer a supportive environment where your skills and passion can thrive. Grow with us as we shape the future of medical care together
                                </p>
                            </div>
                            <img src="/assets/image/careerFormImg.webp" class="img-fluid" alt="">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <form class="careerForm">
                            
                            <div class="form-group">
                                <input type="text" class="form-control" id="career-name" placeholder="Full Name" />
                                <span class="errormsg" id="error-career-name"></span>
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" id="career-phone" placeholder="Phone Number" />
                                <span class="errormsg" id="error-career-phone"></span>
                            </div>
                            <div class="form-group">
                                <input type="email" class="form-control" id="career-email" placeholder="Email Id" />
                                <span class="errormsg" id="error-career-email"></span>
                            </div>
                            <div class="form-group">
                                <select class="form-control" id="career-jobRole">
                                    <option value="">Job Role</option>
                                </select>
                                <span class="errormsg" id="error-career-role"></span>
                            </div>
                            <div class="row">
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <select class="form-control" id="career-state" v-model="selectedState" @change="onStateChange">
                                            <option value="">Select State</option>
                                            <option v-for="state in states" :key="state.name" :value="state.name">
                                                {{ state.name }}
                                            </option>
                                        </select>
                                        <span class="errormsg" id="error-career-state"></span>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <select class="form-control" id="career-city" v-model="selectedCity" :disabled="!selectedState">
                                            <option value="">Select City</option>
                                            <option v-for="city in availableCities" :key="city" :value="city">
                                                {{ city }}
                                            </option>
                                        </select>
                                        <span class="errormsg" id="error-career-city"></span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="resume-upload">
                                    <label for="career-resume" class="resume-label">
                                        <span class="browse-btn">Browse</span>
                                        <span class="upload-text">Upload a resume</span>
                                    </label>
                                    <input type="file" class="form-control" id="career-resume" accept=".pdf,.doc,.docx" hidden @change="handleFileUpload" />
                                    <span class="errormsg" id="error-career-resume"></span>
                                    <div class="file-info">
                                        <span class="selected-file" id="career-selected-file-name"></span>
                                        <span class="remove-file" id="career-remove-file" title="Remove file">×</span>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <select class="form-control" id="career-role" v-model="selectedPosition">
                                    <option value="">Select Role</option>
                                    <option :value="career.title" v-for="career in careers" :key="career.title">{{ career.title }}</option>
                                </select>
                                <span class="errormsg" id="error-career-position"></span>
                            </div>
                            <div class="form-group d-inline-flex gap-3 mb-3">
                                <input type="checkbox" class="mt-1" id="career-terms" />
                                <label for="career-terms" class="terms">
                                    I agree to receive information by signing up on Chettinad Academy of Research & Education
                                </label>
                                <span class="errormsg" id="error-career-terms"></span>
                            </div>
                            <a href="#" class="submitBtn" @click.prevent="submitCareerForm">Submit
                                <span class="material-symbols-outlined">chevron_right</span>
                            </a>
                        </form>
                    </div>
                </div>
            </div>
        </div>


        <div class="testimonialSec">
            <div class="container">
                <h2 class="testimonialHead mb-4 mt-3 text-center">
                    <span class="bg">What</span> our Employees <br>says About Us
                    <img src="/assets/image/lineVector.png" class="lineVector" alt="">
                </h2>
                <div class="splide py-sm-4 py-2 testimonial-slider">
                    <div class="splide__track py-4">
                        <ul class="splide__list">
                            <li class="splide__slide" v-for="testimonial in testimonials">
                                <div class="testimonialCard">
                                    <img src="/assets/image/commaImg.png" class="commaImg img-fluid" alt="">
                                    <h5 class="fw-bold themeText">{{ testimonial?.name }}</h5>
                                    <h4>
                                        {{ testimonial?.description }}
                                        <img src="/assets/image/commaImg2.png" class="img1" alt="">
                                        <img src="/assets/image/commaImg2.png" class="img2" alt="">
                                    </h4>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
    
            </div>
        </div>

        <SuccessPopup :show="showSuccess" @close="closeSuccessPopup" />
        <LoadingSpinner :isLoading="isLoading" />

        <Footer />


    </div>
</template>
<script setup>
import { onMounted, computed, ref } from "vue";
import { statesCitiesData } from '../data/statesCities.js';
import SuccessPopup from '../components/SuccessPopup.vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';

const config = useRuntimeConfig()

const fileToBase64 = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result.split(",")[1]); // only base64 part
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
};

// State and city dropdown data
const selectedState = ref('');
const selectedCity = ref('');
const selectedPosition = ref('');
const states = ref(statesCitiesData);
const isLoading = ref(false);
const showSuccess = ref(false);

// Computed property for available cities based on selected state
const availableCities = computed(() => {
  const state = states.value.find(s => s.name === selectedState.value);
  return state ? state.cities : [];
});

// Method to handle state change
const onStateChange = () => {
  selectedCity.value = ''; // Reset city selection when state changes
};

const careers = [
    {
        title: "Quality & Supply Coordinator",
        experience: "2 -3 yrs Experience",
        qualification: "Diploma in Quality or Supply Chain Management",
        description: 'We’re hiring a Quality & Supply Coordinator to support production and procurement activities across our client projects. The role includes monitoring incoming materials, maintaining quality records, assisting with supplier evaluation, and coordinating with the shop-floor and logistics teams to ensure smooth and compliant operations. You’ll help maintain standards, track non-conformities, and support continuous improvement initiatives.',
        positions: '2',
        date: '10 Jan, 2024'
    }
];

const testimonials = ref([
    {
        name: 'Aravind',
        description: "I'm thrilled to be part of this Company! The supportive team culture, opportunities for growth, and commitment to community make every day rewarding and inspiring.",
    },
]);

onMounted(() => {

    const splide = new Splide(".testimonial-slider", {
        drag: "free",
        focus: 0,
        omitEnd: true,
        snap: true,
        arrows: true,
        indicators: true,
        pagination: true,
        breakpoints: {
            2600: {
                perPage: 1,
            },
            1440: {
                perPage: 1,
            },
            1024: {
                perPage: 1,
            },
            768: {
                perPage: 1,
            },
            576: {
                perPage: 1,
            },
        },
    });
    splide.mount();

});

const applyForCareer = (career) => {
    selectedPosition.value = career.title;
    scrollToForm();
};

const scrollToForm = () => {
    const formSection = document.querySelector('.formSec');
    if (formSection) {
        formSection.scrollIntoView({ behavior: 'smooth' });
    }
};

const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
        const fileName = file.name;
        const selectedFileElement = document.getElementById('career-selected-file-name');
        const removeFileElement = document.getElementById('career-remove-file');
        if (selectedFileElement) {
            selectedFileElement.textContent = fileName;
            selectedFileElement.style.display = 'inline';
        }
        if (removeFileElement) {
            removeFileElement.style.display = 'inline';
        }
    }
};

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

const submitCareerForm = async () => {
  document.querySelectorAll('.errormsg').forEach(el => el.style.display = 'none');

  const name = document.getElementById('career-name').value;
  const phone = document.getElementById('career-phone').value;
  const email = document.getElementById('career-email').value;
  const jobRole = document.getElementById('career-jobRole').value;
  const state = selectedState.value;
  const city = selectedCity.value;
  const position = selectedPosition.value;
  const terms = document.getElementById('career-terms').checked;

  // Validation (kept same as yours)
  if (!name) return showError('#error-career-name', 'Name cannot be blank');
  if (!phone) return showError('#error-career-phone', 'Phone cannot be blank');
  if (!validatePhone(phone)) return showError('#error-career-phone', 'Invalid phone number');
  if (!email) return showError('#error-career-email', 'Email cannot be blank');
  if (!validateEmail(email)) return showError('#error-career-email', 'Invalid email');
  if (!state) return showError('#error-career-state', 'State cannot be blank');
  if (!city) return showError('#error-career-city', 'City cannot be blank');
  if (!position) return showError('#error-career-position', 'Position cannot be blank');
  if (!terms) return showError('#error-career-terms', 'Please accept terms');

  // prepare loading state
  isLoading.value = true;
  const submitBtn = document.querySelector('.submitBtn');
  const originalText = submitBtn.innerHTML;
  submitBtn.innerHTML = 'Submitting...';
  submitBtn.disabled = true;

  // Build fields for email body
  const fields = {
    "Name": name,
    "Phone Number": phone,
    "Email": email,
    "Job Role": jobRole,
    "State": state,
    "City": city,
    "Applied Position": position
  };

  // Build admin email message
  let emailMsg1 = "Hello Admin,<br><br>"
                + "A new career application has been submitted.<br><br>";
  Object.entries(fields).forEach(([key, value]) => {
    emailMsg1 += `${key}: ${value}<br/>`;
  });

  emailMsg1 += "<br>Best regards,<br>Primal Solutions Website";

  // Build user message
  let emailMsg2 = `Hi ${name},<br><br>
      Thank you for applying. Our team will reach out soon.<br><br>
      Regards,<br>Primal Solutions`;

  // ⭐ HANDLE RESUME UPLOAD → BASE64
  const resumeInput = document.getElementById('career-resume');
  let attachment = null;

  if (resumeInput.files.length > 0) {
    const file = resumeInput.files[0];
    const base64 = await fileToBase64(file);

    attachment = {
      filename: file.name,
      contentType: file.type || "application/octet-stream",
      base64: base64
    };
  }

  // ⭐ FINAL EMAIL DATA SENT TO SERVER
  const emailData = {
    adminEmail: {
      to: "ganeshraju@mocerohealth.in",
      cc: "ganeshraju@mocerohealth.in",
      subject: "Career Application - Primal Solutions",
      html: emailMsg1
    },
    userEmail: {
      to: email,
      cc: email,
      subject: "Thank you for applying",
      html: emailMsg2
    },
    attachment // <---- THIS IS WHAT SENDS THE RESUME
  };

  try {
    const response = await fetch(config.public.emailApi, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(emailData)
    });

    const data = await response.json();

    if (data.status === true) {
      // reset form
      document.getElementById('career-name').value = '';
      document.getElementById('career-phone').value = '';
      document.getElementById('career-email').value = '';
      document.getElementById('career-jobRole').value = '';
      selectedState.value = '';
      selectedCity.value = '';
      selectedPosition.value = '';
      document.getElementById('career-terms').checked = false;
      document.getElementById('career-resume').value = '';
      document.getElementById('career-selected-file-name').textContent = '';
      document.getElementById('career-remove-file').style.display = 'none';

      submitBtn.innerHTML = originalText;
      submitBtn.disabled = false;
      isLoading.value = false;
      showSuccess.value = true;
    } else {
      throw new Error("Failed to send email");
    }
  } catch (error) {
    console.error("Error submitting:", error);
    showError('#error-career-name', 'Failed to submit application');
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;
    isLoading.value = false;
  }
};

// Close success popup function
const closeSuccessPopup = () => {
  showSuccess.value = false
}

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.careersBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/careersBnr.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
.careersBnr h1{
    color: #fff;
}
.careersBnr .content {
    height: 90vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}
.careersBnr .content h1 {
    font-size: 60px;
}
.whyUsCard{
    background-color: #fff;
    padding: 2em 3em;
    color: #fff;
}
.whyUsCard h3{
    font-size: 2.8rem;
}

.careerCard{
    background-color: #fff;
    padding: 2em 3em;
    margin-bottom: 30px;
    border-radius: 8px;
    border: 1px solid #e1e1e1;
}
.careerCard:hover{
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
}
.careerCard span{
    color: #999;
}
.careerCard .careerDate{
    margin-left: 15px;
    padding-left: 15px;
    border-left: 1px solid #e1e1e1;
}
.careerCard .applySection{
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.careerCard .applyBtn{
    background-color: #111F61;
    color: #fff;
    padding: 10px 35px;
    border: none;
    border-radius: 5px;
}
.careerForm{
    width: 80%;
    margin: 0 auto;
    margin-bottom: 40px;
}
.careerForm input{
    color: #fff;
}
.careerForm input, .careerForm select{
    color: #fff;
    height: 50px;
    background-color: #ffffff3c !important;
    border: none;
    margin-bottom: 25px;
}
.careerForm select option{
    background-color: #999;
}
.careerForm input[type=checkbox]{
    width: 15px;
    height: 15px;
    aspect-ratio: 1/1;
    display: inline;
    margin: 0;
    padding: 0;
    border-radius: 5px;
    border: none;
    outline: none;
}
.careerForm input::placeholder, .careerForm select::placeholder{
    color: #fff;
}
.careerForm .submitBtn{
    background-color: #fff;
    border-radius: 40px;
    color: #111F61;
    display: flex;
    gap: 10px;
    justify-content: center;
    padding: 12px;
    text-decoration: none;
}
.resume-upload {
    margin-bottom: 25px;
}
.resume-label {
    display: flex;
    align-items: center;
    width: 100%;
    height: 50px;
    background-color: #ffffff3c !important;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    overflow: hidden;
}
.browse-btn {
    display: inline-block;
    padding: 5px 15px;
    background-color: #ffffff4c;
    border-radius: 15px;
    font-size: 12px;
    color: #fff;
    margin: 12px;
}
.upload-text {
    color: #fff;
    font-size: 14px;
}
.file-info {
    display: flex;
    align-items: center;
    margin-top: 5px;
}
.selected-file {
    font-size: 12px;
    color: #fff;
    margin-right: 5px;
}
.remove-file {
    display: none;
    font-size: 14px;
    color: #ff5252;
    cursor: pointer;
    font-weight: bold;
    margin-left: 5px;
}
.errormsg {
    color: #dc3545;
    font-size: 14px;
    display: none;
    margin-top: -20px;
    margin-bottom: 15px;
}
.careerForm .terms  {
    font-size: 14px;
    color: #fff;
}
.testimonialSec{
    padding: 4em 0;
    background-image: url('/assets/image/employeesBg.webp');
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
}
.testimonial-slider{
    width: 70%;
    margin: 0 auto;
}
.testimonialHead{
    position: relative;
}
.testimonialHead .bg{
    background-color: #0D248C;
    padding: 0px 10px;
    border-radius: 20px;
    color: #fff;
}
.testimonialHead .lineVector{
    width: 30%;
    max-width: 200px;
    position: absolute;
    bottom: -30px;
    left: 55%;
    transform: translateX(-50%);
}
.testimonialCard{
    background: #C9CDE1;
    background-repeat: no-repeat;
    background-position: top right;
    background-size: contain;
    color: #444444;
    padding: 4em 2em;
    border-radius: 35px;
    margin: 0 6px;
    position: relative;
    text-align: center;
}
.testimonialCard .userImg{
    width: 40px;
    height: 40px;
    aspect-ratio: 1/1;
    border-radius: 50%;
}
.testimonialCard h4{
    color: #444444;
    line-height: 1.6;
    width: 78%;
    margin: 20px auto;
    position: relative;
}
.testimonialCard h4 .img1{
    position: absolute;
    top: -10%;
    left: -4%;
    width: 10%;
    max-width: 100px;
}
.testimonialCard h4 .img2{
    position: absolute;
    bottom: -10%;
    right: -4%;
    width: 10%;
    max-width: 100px;
    transform: rotate(180deg);
}
.testimonialCard h5{
    margin-bottom: 0;
}
.testimonialCard .starImg{
    width: 80px;
}
.testimonialCard .commaImg{
    position: absolute;
    bottom: 10%;
    right: 4%;
    width: 20%;
    max-width: 150px;
    margin-bottom: 10px;
}
.formSec img{
    width: 75% !important;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    .careersBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .careersBnr .content h1 {
        font-size: 44px;
    }
}
@media only screen and (max-width:830px) {
    .careersBnr .content h1 {
        font-size: 40px;
    }
    .formSec{
        flex-direction: column-reverse;
    }
    .formSec img{
        width: 70% !important;
        margin: 0 auto;
    }
    .testimonial-slider{
        width: 90%;
    }
    .testimonialCard{
        padding: 2em 1em;
    }
}
@media only screen and (max-width:578px) {
    .whyUsCard{
        padding: 1em 1.5em;
    }
    .whyUsCard h3 {
        font-size: 1.8rem;
    }
    .careerCard .applySection{
        flex-direction: column;
    }
    .formSec img{
        width: 80% !important;
    }
    .testimonial-slider{
        width: 100%;
    }
    .testimonialCard{
        padding: 2em 1em;
    }
    .testimonialCard h4{
        font-size: 1rem;
        width: 88%;
    }
}
</style>