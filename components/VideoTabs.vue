<template>

    <div class="row">
        <!-- Left: Main Video -->
        <div class="col-sm-8 mb-4 mb-lg-0">
            <div class="mainVideoWrapper">
                <video 
                    :src="videos[selectedVideoIndex].videoUrl" 
                    class="mainVideo" 
                    controls
                    >
                </video>
            </div>
        </div>
                    
        <!-- Right: Video Thumbnails -->
        <div class="col-sm-4">
            <div class="videoThumbnailsContainer">
                <div 
                    v-for="(video, index) in videos" 
                    :key="index"
                    class="videoThumbnail"
                    :class="{ 'active': selectedVideoIndex === index }"
                    @click="selectedVideoIndex = index"
                >
                    <video class="thumbnail-video">
                        <source :src="video.videoUrl" type="video/mp4">
                    </video>
                    <div class="playButton">
                        <span class="material-symbols-outlined">play_circle</span>
                    </div>
                    <p class="thumbnail-title">{{ video.title }}</p>
                </div>
            </div>
        </div>
    </div>

</template>
<script setup>
import { onMounted } from "vue";
const props = defineProps({
    videos: {
        type: Object,
        required: true,
    },
});

const selectedVideoIndex = ref(0);

</script>
<style scoped>
    .mainVideoWrapper {
    width: 100%;
    aspect-ratio: 16 / 9;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.mainVideo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    aspect-ratio: 421/237;
}

.videoThumbnailsContainer {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.videoThumbnail {
    position: relative;
    cursor: pointer;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    border: 3px solid transparent;
    /* aspect-ratio: 16 / 9; */
    aspect-ratio: 421/237;
}

.videoThumbnail.active {
    border-color: #111F61;
    box-shadow: 0 6px 20px rgba(17, 31, 97, 0.2);
}

.thumbnail-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.videoThumbnail:hover .thumbnail-video {
    transform: scale(1.05);
}

.playButton {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.3s ease;
}

.playButton span {
    font-size: 48px;
    color: #fff;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.videoThumbnail:hover .playButton {
    opacity: 1;
}

.thumbnail-title {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
    color: #fff;
    padding: 1rem;
    margin: 0;
    font-size: 14px;
    font-weight: 500;
}


@media only screen and (max-width:1080px) {
    .videoThumbnailsContainer {
        gap: 1rem;
    }
}
@media only screen and (max-width:578px) {
    .videoThumbnailsContainer{
        flex-direction: row;
    }
    .videoThumbnail{
        width: 48%;
    }
    .thumbnail-title{
        font-size: 12px;
    }
}

</style>