<template>

    <div class="galleryCard">
        <div class="image-wrapper" @click="showPopup = true">
            <img :src="`${gallery.image}`" class="img-fluid" :alt="gallery.title" />
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
                <h3>{{ gallery.title }}</h3>
                    <img :src="currentImage" class="popup-image" :alt="`Gallery image for ${gallery.title}`" />
                    <div
                        v-for="(img, index) in gallery.images"
                        :key="index"
                        class="thumbnail-item"
                        :class="{ active: selectedIndex === index }"
                        @click.stop="selectedIndex = index"
                    >
                        <img :src="img" :alt="`Thumbnail ${index + 1} for ${gallery.title}`" />
                    </div>
                </div>
            </div>
        
    </transition>

</template>
<script setup>
import { ref, computed, watch } from "vue";
const props = defineProps({
    gallery: {
        type: Object,
        required: true,
    },
});

const showPopup = ref(false);
const selectedIndex = ref(0);

const hasMultipleImages = computed(() => Array.isArray(props.gallery.images) && props.gallery.images.length > 1);
const currentImage = computed(() => {
    if (Array.isArray(props.gallery.images) && props.gallery.images.length > 0) {
        return props.gallery.images[selectedIndex.value];
    }
    return props.gallery.image;
});

watch(showPopup, (val) => {
    if (val) {
        selectedIndex.value = 0;
    }
});
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
    /* background: #fff; */
    border-radius: 12px;
    /* padding: 2rem; */
    max-width: 80vw;
    /* width: 90%;
    max-height: 90vh; */
    /* overflow-y: auto; */
    /* box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); */
}

.close-btn {
  position: absolute;
  top: -10px;
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
  max-height: 500px;
  object-fit: cover;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.popup-thumbnails {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  margin-top: 1.5rem;
  overflow-x: auto;
  padding-bottom: 0.25rem;
  flex-wrap: wrap;
}

.thumbnail-item {
  border: 3px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  overflow: hidden;
  width: 80px;
  height: 56px;
  cursor: pointer;
  flex: 0 0 auto;
  transition: all 0.3s ease;
}

.thumbnail-item:hover {
  border-color: rgba(255, 255, 255, 0.4);
  transform: scale(1.05);
}

.thumbnail-item.active {
  border-color: #fff;
}

.thumbnail-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popup-content h3 {
  color: #fff;
  margin: 1.5rem 0 0.75rem 0;
  font-size: 1.5rem;
  font-weight: 600;
  text-align: center;
}

/* .popup-content p {
  color: #555;
  margin: 0 0 1.5rem 0;
  line-height: 1.6;
  text-align: center;
} */

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
    .popup-content {
        padding: 1.5rem;
        width: 95%;
    }
    
    .popup-content h3 {
        font-size: 1.25rem;
    }
    
    .popup-thumbnails {
        gap: 0.5rem;
    }
    
    .thumbnail-item {
        width: 70px;
        height: 49px;
    }
}
@media only screen and (max-width:578px) {
    .popup-content {
        padding: 1rem;
        width: 98%;
    }
    
    .popup-image {
        max-height: 300px;
    }
    
    .popup-content h3 {
        font-size: 1.1rem;
        margin: 1rem 0 0.5rem 0;
    }
    
    .popup-content p {
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .popup-thumbnails {
        gap: 0.4rem;
        margin-top: 1rem;
    }
    
    .thumbnail-item {
        width: 60px;
        height: 42px;
    }
    
    .close-btn {
        top: -30px;
        right: -20px;
        font-size: 30px;
    }
}
</style>