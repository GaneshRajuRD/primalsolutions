<template>
    <div class="realResultsSec py-5" v-if="videos.length > 0">
        <div class="container">
            <h2 class="realResultsTitle mb-5"><span class="fw-bold">Transformation</span> in Action</h2>
            <VideoTabs :videos="videos" />
        </div>
    </div>
</template>

<script setup>
defineProps({
    videos: {
        type: Array,
        required: true,
    },
});
</script>

<style scoped>
.realResultsSec {
    background-color: #F0F3FF;
}

.realResultsTitle {
    font-size: 48px;
    margin-bottom: 3rem;
}

@media only screen and (max-width: 1080px) {
    .realResultsTitle {
        font-size: 36px;
    }
}
</style>
