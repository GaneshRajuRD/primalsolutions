<template>
  <main class="serviceSlider">
    <h4 class="gearIcon2 fw-bold text-white serviceTitle">OUR SERVICES</h4>
    <div class="slider" ref="slider">
      <div v-for="item in items" :key="item.id" class="item">
        <img :src="item.image" loading="eager" :alt="item.title">
        <div class='content'>
          <h1 class='title'>{{ item.title }}</h1>
          <p class='description'>{{ item.description }}</p>
          <NuxtLink :to="`/services/${item.link}`" class="link">View More</NuxtLink>
        </div>
      </div>
    </div>
    <nav class='nav'>
      <span class="material-symbols-outlined btn prev" name="arrow-back-outline" @click="prev">arrow_back</span>
      <span class="material-symbols-outlined btn next" name="arrow-forward-outline" @click="next">arrow_forward</span>
      <!-- <ion-icon class=''></ion-icon>
      <ion-icon class=''></ion-icon> -->
    </nav>
  </main>
</template>
<script>
export default {
  name: 'ServiceSlider',
  data() {
    return {
      items: [
        {
          id: 1,
          title: 'Market Research & Intelligence Services',
          description: 'We provide industry insights that help you make confident decisions, explore new markets, and stay ahead of trends.',
          image: '/assets/image/Market-Research-service.webp',
          link: 'market-research-intelligence-services'
        },
        {
          id: 2,
          title: 'Business Strategy',
          description: 'We turn vision into clear, data-driven strategies that deliver measurable and sustainable growth.',
          image: '/assets/image/Business-Strategy-service.webp',
          link: 'business-strategy'
        },
        {
          id: 3,
          title: 'Plant Layout Design & Optimization',
          description: 'We design and optimize plant layouts that enhance flow efficiency, maximize space utilization, and enable scalable growth.',
          image: '/assets/image/Business-Transformation-service.webp',
          link: 'plant-layout-design-optimization'
        },
        {
          id: 4,
          title: 'Operational Excellence & Lean Transformation',
          description: 'We drive operational excellence by embedding lean principles, optimizing processes, and building sustainable high-performance workplaces.',
          image: '/assets/image/Operations-Supply-Chain-Excellence-service.webp',
          link: 'operational-excellence-lean-transformation'
        },
        {
          id: 5,
          title: 'Zero Defect Culture Deployment',
          description: 'We foster a Zero Defect culture by strengthening QMS, embedding preventive quality systems, and integrating DWM for effective daily monitoring and continuous improvement.',
          image: '/assets/image/zero-defect-culture-deployment.webp',
          link: 'zero-defect-culture-deployment'
        },
        {
          id: 6,
          title: 'Digital & Smart Factory Transformation',
          description: 'We enable smart factory transformation through integrated digital systems, VCS-driven real-time monitoring, digital quality management, and predictive analytics.',
          image: '/assets/image/Smart-factory-tarnsformation.webp',
          link: 'digital-smart-factory-transformation'
        },
        {
          id: 7,
          title: 'Supplier Capability and Performance Enhancement',
          description: 'We strengthen supplier capability, quality, and delivery performance to achieve operational excellence and improved OEM rankings.',
          image: '/assets/image/Supplier-Performance.webp',
          link: 'supplier-capability-performance-enhancement'
        },
        {
          id: 8,
          title: 'Skill development programs and certifications',
          description: 'We build organizational capability through structured skill development, ESG implementation, and certification readiness programs.',
          image: '/assets/image/Skill-Developement.webp',
          link: 'skill-development-programs-certifications'
        },
        {
          id: 9,
          title: 'Talent Hiring & Management Services',
          description: 'We design end-to-end talent acquisition and management solutions to attract, develop, and retain high-performing teams aligned with business goals.',
          image: '/assets/image/Talent-Hiring-Management-service.webp',
          link: 'talent-hiring-management-services'
        }
      ]
    }
  },
  methods: {
    next() {
      const slider = this.$refs.slider;
      const items = slider.querySelectorAll('.item');
      slider.append(items[0]);
    },
    prev() {
      const slider = this.$refs.slider;
      const items = slider.querySelectorAll('.item');
      slider.prepend(items[items.length - 1]);
    }
  }
}
</script>

<style>
/* home page slider */

.serviceSlider .item:nth-child(2)::after{
    background-image: linear-gradient(to bottom,rgb(16, 15, 35,0.2),rgb(16, 15, 35,0.2));
    background-blend-mode: soft-light;
}

:root {
    --width: 20%;
    --gap: 1rem;
    --speed: 500ms;
  }

  .serviceSlider {
    position: relative;
    overflow: hidden;
    height: 100vh;
    background: #202227;
  }
  .serviceTitle{
    position: absolute;
    top: 12%;
    left: 3%;
    z-index: 5;
  }

  .serviceSlider .slider {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
  }

  .serviceSlider .item {
    display: flex;
    align-items: center;
    width: var(--width);
    height: calc(var(--width) * 1.5);
    position: absolute;
    z-index: 1;
    border-radius: 0.25rem;
    box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 1);
    transition: left var(--speed), width var(--speed), height var(--speed), border-radius var(--speed), opacity var(--speed);
    transition-timing-function: ease-out;
    transform-origin: center;
    overflow: hidden;
    will-change: transform, opacity;
    border-radius: 30px;
    border: 3px solid #fff;
  }

  .serviceSlider .item::after {
    content: "";
    display: block;
    position: absolute;
    inset: 0;
    z-index: 0;
    box-shadow: 0px 0px 50px 25px rgba(0, 0, 0, 0.25) inset;
    transition: box-shadow var(--speed);
    will-change: transform, opacity;
  }

  .serviceSlider .item img {
    position: relative;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .serviceSlider .item:nth-child(1),
  .serviceSlider .item:nth-child(2) {
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 0;
    box-shadow: none;
    border: none !important;
    opacity: 1;
    filter: blur(0);
  }

  .serviceSlider .item:nth-child(9){
    /* visibility: hidden; */
  }

  .serviceSlider .item:nth-child(1)::after,
  .serviceSlider .item:nth-child(2)::after {
    box-shadow: 0px -50px 150px 50px rgba(0, 0, 0, 0.75) inset;
  }

  .serviceSlider .item:nth-child(2)::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image: linear-gradient(to bottom, transparent, #15182f);
    filter: blur(5px);
    z-index: 1;
  }

  .serviceSlider .item:nth-child(3) {
    left: 50%;
    height: calc(var(--width) * 2);
    bottom: 10%;
  }

  .serviceSlider .item:nth-child(4) {
    left: calc(50% + var(--width) + var(--gap));
    transition-delay: calc(var(--speed) * 0.2);
    border: none !important;
    width: 20% !important;
    bottom: 10%;
  }

  .serviceSlider .item:nth-child(5) {
    left: calc(50% + calc(var(--width) * 2) + calc(var(--gap) * 2));
    transition-delay: calc(var(--speed) * 0.4);
    bottom: 10%;
  }

  .serviceSlider .item:nth-child(6) {
    left: calc(50% + calc(var(--width) * 3) + calc(var(--gap) * 3));
    opacity: 0;
    transition-delay: calc(var(--speed) * 0.6);
  }

  .serviceSlider .item:nth-child(7) {
    left: calc(50% + calc(var(--width) * 4) + calc(var(--gap) * 4));
    opacity: 0;
    transition-delay: calc(var(--speed) * 0.8);
  }

  .serviceSlider .item:nth-child(8) {
    left: calc(50% + calc(var(--width) * 5) + calc(var(--gap) * 5));
    opacity: 0;
    transition-delay: calc(var(--speed) * 1.0);
  }

  .serviceSlider .item:nth-child(9) {
    left: calc(50% + calc(var(--width) * 6) + calc(var(--gap) * 6));
    opacity: 0;
    transition-delay: calc(var(--speed) * 1.2);
  }

  .serviceSlider .content {
    width: min(35vw, 450px);
    position: absolute;
    left: 3rem;
    z-index: 1;
    transform: translateY(25%);
    color: white;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.75);
    opacity: 0;
    display: none;
    flex-direction: column;
    gap: 1rem;
    outline: 0;
  }

  .serviceSlider .content * {
    outline: 0;
  }

  .serviceSlider .content .title {
    font-weight: 600;
    color: #fff;
    text-transform: uppercase;
  }

  .serviceSlider .content .description {
    line-height: 1.7;
  }

  .serviceSlider .content .link {
    width: fit-content;
    background-color: #0D248C;
    color: #fff;
    border: 0;
    border-radius: 10px;
    padding: 6px 20px;
    cursor: pointer;
    transition: background var(--speed), color var(--speed);
    text-decoration: none;
  }

  .serviceSlider .content .link:hover {
    background-color: #fff;
    color: #0D248C;
  }

  .serviceSlider .item:nth-of-type(2) .content {
    display: flex;
    animation: show var(--speed) ease-in-out calc(var(--speed) / 2) forwards;
  }

  @keyframes show {
    0% {
      filter: blur(10px);
    }
    100% {
      opacity: 1;
      filter: blur(0);
      transform: translateY(0);
    }
  }

  .serviceSlider .nav {
    display: flex;
    gap: 0.5rem;
    position: absolute;
    top: 2rem;
    right: 2%;
    transform: translateX(-50%);
    z-index: 5;
    user-select: none;
    border-radius: 100vw;
    padding: 0.25rem;
  }

  .serviceSlider .nav .btn {
    background-color: transparent;
    color: #fff;
    padding: 0.75rem;
    border-radius: 50%;
    cursor: pointer;
    transition: background var(--speed), color var(--speed);
    border: 2px solid #fff;
  }

  .serviceSlider .nav .btn:hover {
    background-color: #fff;
    color: #444;
  }

  @media (width > 650px) and (width < 900px) {
    .serviceSlider .content .title {
      font-size: 1rem;
    }

    .serviceSlider .content .description {
      font-size: 0.7rem;
    }

    .serviceSlider .content button {
      font-size: 0.7rem;
    }

    .serviceSlider .item {
      width: 25%;
      height: 26%;
    }

    .serviceSlider .item:nth-child(3) {
      left: 50%;
      height: calc(var(--width) * 1.4);
    }

    .serviceSlider .item:nth-child(4) {
      left: calc(50% + 28%);
    }

    .serviceSlider .item:nth-child(5) {
      left: calc(50% + 60%);
    }

    .serviceSlider .item:nth-child(6) {
      left: calc(50% + 80%);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(7) {
      left: calc(50% + 100%);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(8) {
      left: calc(50% + 120%);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(9) {
      left: calc(50% + 140%);
      opacity: 0;
    }
  }

  @media (width < 650px) {
    .serviceSlider .content {
      width: 90%;
      top: 20%;
    }

    .serviceSlider .content .title {
      font-size: 0.9rem;
    }

    .serviceSlider .content .description {
      font-size: 0.75rem;
    }

    .serviceSlider .content button {
      font-size: 0.7rem;
    }

    .serviceSlider .item {
      width: 45%;
      height: 34%;
    }

    .serviceSlider .item:nth-child(3) {
      left: 15%;
      height: calc(var(--width) * 1);
    }

    .serviceSlider .item:nth-child(4) {
      left: calc(50% + 15%);
      width: 30% !important;
      height: 17%;
    }

    .serviceSlider .item:nth-child(5) {
      left: calc(50% + 280px);
    }

    .serviceSlider .item:nth-child(6) {
      left: calc(50% + 420px);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(7) {
      left: calc(50% + 500px);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(8) {
      left: calc(50% + 580px);
      opacity: 0;
    }

    .serviceSlider .item:nth-child(9) {
      left: calc(50% + 660px);
      opacity: 0;
    }
  }

/* home page slider */
</style>
