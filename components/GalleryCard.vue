<template>

    <div class="galleryCard">
        <div class="image-wrapper" @click="showPopup = true">
            <img :src="`${gallery.image}`" class="img-fluid" />
        </div>
        <div class="content">
            <h5 class="mb-2">{{ gallery.title }}</h5>
        </div>
    </div>

    <!-- Gallery Popup -->
    <transition name="fade">
        <div v-if="showPopup" class="gallery-popup" @click="showPopup = false">
            <div class="popup-content" @click.stop>
                <button class="close-btn" @click="showPopup = false">&times;</button>
                <img :src="`${gallery.image}`" class="popup-image" />
                <h3>{{ gallery.title }}</h3>
                <p v-if="gallery.description">{{ gallery.description }}</p>
            </div>
        </div>
    </transition>

</template>
<script setup>
import { ref } from "vue";
const props = defineProps({
    gallery: {
        type: Object,
        required: true,
    },
});

const showPopup = ref(false);

</script>
<style scoped>
.galleryCard{
    color: #444;
    margin-bottom: 15px;
    overflow: hidden;
    margin: 0 10px 20px;
}
.galleryCard:hover img{
    transition: all 0.5s ease;
}
.galleryCard a{
    text-decoration: none;
    color: #444;
}
.galleryCard img{
    width: 100%;
    border-radius: 20px;
    margin-bottom: 15px;
    aspect-ratio: 336/224;
    object-fit: cover;
}
.galleryCard h5{
    color: #444;
    margin: 0;
}
.image-wrapper {
    border-radius: 20px;
    aspect-ratio: 336/224;
    overflow: hidden;
    position: relative;
    margin-bottom: 25px;
    cursor: pointer;
}

.image-wrapper img {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: translate(-50%, -50%); /* Keep image centered */
  transition: width 0.5s ease, height 0.5s ease;
}

.image-wrapper:hover img {
  width: 115%;
  height: 115%;
}

/* Gallery Popup Styles */
.gallery-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000;
}

.popup-content {
    position: relative;
}

.close-btn {
  position: absolute;
  top: -40px;
  right: -30px;
  background: none;
  border: none;
  font-size: 40px;
  cursor: pointer;
  color: #fff;
  transition: color 0.3s;
}

.close-btn:hover {
  transform: scale(1.2);
  transition: 0.3s ease-in-out;
}

.popup-image {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  max-height: 400px;
  object-fit: cover;
}

.popup-content h3 {
  color: #444;
  margin: 1rem 0 0.5rem;
  font-weight: bold;
}

.popup-content p {
  color: #666;
  margin: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    
}
@media only screen and (max-width:1080px) {
    
}
@media only screen and (max-width:830px) {
    
}
@media only screen and (max-width:578px) {
    
}
</style>