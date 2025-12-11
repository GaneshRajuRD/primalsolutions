<template>
  <NuxtLink to="/contact-us">

    <div class="floating-widget"  type="" data-bs-toggle="modal" data-bs-target="#RegisterPopup">
      <div class="widget-wrapper">
        <div class="curved-text">
          <svg viewBox="0 0 100 100">
            <defs>
              <path id="curve" d="M 50,50 m -37,0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0" />
            </defs>
            <text>
              <textPath href="#curve" startOffset="0%">
                Contact us*Contact us
              </textPath>
            </text>
          </svg>
        </div>
        <div class="widget-circle">
          <img src="/assets/image/arrowImg.png" alt="Mocero" class="widget-icon">
        </div>
        <div class="bottom-curved-text">
          <svg viewBox="0 0 100 100">
            <defs>
              <!-- <path id="bottom-curve" d="M 13,50 a 37,37 0 0,0 74,0" /> -->
              <path id="bottom-curve" d="M 50,50 m -37,0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0" />
            </defs>
            <text>
              <textPath href="#bottom-curve" startOffset="50%">
                Contact us*Contact us
              </textPath>
            </text>
          </svg>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const emit = defineEmits(['bookDemo']);
</script>

<style scoped>
.floating-widget {
  position: absolute;
  bottom: 50%;
  right: 50%;
  transform: translate(60%, 50%);
  z-index: 50;
  cursor: pointer;
  user-select: none;
}

.widget-wrapper {
  position: relative;
  width: 115px;
  height: 115px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.curved-text {
  position: absolute;
  width: 100%;
  height: 100%;
  animation: rotate 20s linear infinite;
  z-index: 3;
}

.curved-text svg {
  width: 100%;
  height: 100%;
}

.curved-text text {
  fill: #fff;
  /* fill: #444; */
  font-size: 10px;
  font-weight: bold;
  /* letter-spacing: 1px; */
}
.curved-text textpath{
  position: relative;
}
.curved-text textpath::before{
  content: '';
  position: absolute;
  background: #fff;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  top: 50%;
  left: 50%;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.widget-circle {
  width: 100%;
  height: 100%;
  background: #1E35BC;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  transition: transform 0.3s ease;
  animation: pulse 2s infinite;
}

.widget-icon {
  width: 40px;
  height: 40px;
  position: relative;
}

.bottom-curved-text {
  position: absolute;
  width: 100%;
  height: 100%;
  /* top: 75px; */
  /* left: 50%; */
  transform: translateX(-50%);
  animation: rotate 20s linear infinite;
  z-index: 2;
}

.bottom-curved-text svg {
  width: 100%;
  height: 100%;
}

.bottom-curved-text text {
  fill: #fff;
  font-size: 10px;
  font-weight: bold;
  /* letter-spacing: 1px; */
}

.widget-wrapper:hover .curved-text {
  animation-play-state: paused;
}
.widget-wrapper:hover .bottom-curved-text {
  animation-play-state: paused;
}

.widget-circle:hover {
  transform: scale(1.03);
}


/* Responsive adjustments */
@media (max-width: 1290px) {
  .widget-circle {
    width: 100%;
    height: 100%;
    animation-duration: 25s, 2s;
  }
  .widget-icon {
    width: 40px;
    height: 40px;
  }


}
@media (max-width: 830px) {
  .floating-widget {
    width: 125px;
    height: 125px;
    top: -62px;
    right: 50%;
    transform: translate(60%, 0%);
  }
  .widget-wrapper{
    width: 125px;
    height: 125px;
  }
  
  .widget-circle {
    width: 100%;
    height: 100%;
    animation-duration: 25s, 2s; /* Slower rotate on mobile */
  }
  
  .letter {
    font-size: 9px;
    transform: 
    translate(-50%, -50%) 
    rotate(var(--angle)) 
    translateY(-30px) 
    rotate(calc(-1 * var(--angle)));
  }
  
  .widget-icon {
    width: 55px;
    height: 55px;
  }
  .curved-text {
    width: 110%;
    height: 110%;
  }

  .bottom-curved-text {
    width: 110%;
    height: 110%;
  }
  .curved-text text{
    font-size: 9px;
  }
  .bottom-curved-text text{
    font-size: 9px;
  }
}
@media (max-width: 578px) {
  .curved-text {
    width: 110%;
    height: 110%;
  }
}

</style>
