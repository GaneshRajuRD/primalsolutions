<template>

    <div class="caseStudyCard">
        <NuxtLink :to="`/case-study/`+ caseStudy.url">
        <!-- <NuxtLink to="#"> -->
            <img :src="caseStudy.image" class="caseStudyImg" alt="" />
            <div class="info">
                <span>
                    <img src="/assets/image/clockVector.png" class="vector" alt="">
                    {{ caseStudy.readtime }}
                </span>
                <span> | </span>
                <span>
                    <img src="/assets/image/clockVector.png" class="vector" alt="">
                    {{ caseStudy.date }}
                </span>
            </div>
            <h5 class="mb-4">{{ caseStudy.title }}</h5>
            <a href="#" class="link">
                View Case Study
            </a>
        </NuxtLink>
    </div>

</template>

<script setup>
import { onMounted } from "vue";
const props = defineProps({
    caseStudy: {
        type: Object,
        required: true,
    },
});

</script>
<style scoped>
.caseStudyCard{
    background-color: #fff;
    padding: 2.2em;
    border-radius: 15px;
    margin: 0 15px;
}
.caseStudyCard a{
    text-decoration: none;
    color: black;
}
.caseStudyCard .caseStudyImg{
    width: 100%;
    border-radius: 20px;
    margin-bottom: 20px;
    aspect-ratio: 688/390;
}
.caseStudyCard .link{
    background-color: #F7F7F8;
    border: 1px solid #E4E4E7;
    border-radius: 50px;
    padding: 15px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.caseStudyCard .info{
    background-color: #F7F7F8;
    border: 1px solid #E4E4E7;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    width: max-content;
    padding: 10px 15px;
    border-radius: 40px;
    font-size: 14px;
    color: #4C4C4D;
    margin-bottom: 20px;
}
.caseStudyCard .info img.vector{
    width: 14px;
    height: 14px;
    margin-right: 5px;
}
.caseStudyCard span{
    display: flex;
    align-items: center;
}



@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    
}
@media only screen and (max-width:1080px) {
    
}
@media only screen and (max-width:830px) {
    .caseStudyCard{
        padding: 1.4em;
    }
    .caseStudyCard .info{
        font-size: 12px;
        padding: 5px 10px;
    }
    .caseStudyCard h5{
        font-size: 1rem;
    }
}
@media only screen and (max-width:578px) {
    .caseStudyCard{
        margin: 0 5px;
    }
}

</style>