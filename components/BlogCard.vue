<template>

    <div class="blogCard">
        <!-- <NuxtLink :to="`/blogs/`+ blog.url"> -->
        <NuxtLink to="#">
            <img :src="blog.image" class="blogImg" alt="" />
            <div class="row">
                <div class="col-10 col-sm-8">
                    <p>{{ blog.title }}</p>
                </div>
                <div class="col-0 col-sm-2 px-0"></div>
                <div class="col-2 d-flex justify-content-end">
                    <a href="#" class="link">
                        <img src="/assets/image/arrowImg.png" alt="arrow-right" />
                    </a>
                </div>
            </div>
        </NuxtLink>
    </div>

</template>

<script setup>
import { onMounted } from "vue";
const props = defineProps({
    blog: {
        type: Object,
        required: true,
    },
});

</script>
<style scoped>
.blogCard a{
    text-decoration: none;
    color: black;
}
.blogCard .blogImg{
    width: 100%;
    border-radius: 20px;
    margin-bottom: 20px;
    aspect-ratio: 688/390;
}
.blogCard .link{
    background-color: #132162;
    border-radius: 10px;
    padding: 5px;
    height: 30px;
    width: 30px;
    aspect-ratio: 1/1;
    display: flex;
    justify-content: center;
    align-items: center;
}
.blogCard .link img{
    width: 20px;
    height: 20px;
    object-fit: contain;
}

.blogCard{
    margin: 0 15px !important;
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
    .blogCard{
        margin: 0 5px !important;
    }
}

</style>