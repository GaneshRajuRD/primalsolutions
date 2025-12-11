<template>

    <div class="teamMemberCard">
        <div class="blueBg"></div>
        <h2 class="position fw-bold">{{ teamMember.title }}</h2>
        <div class="row">
            <div class="col-9 col-sm-6">
                <div class="h-100 d-flex flex-column justify-content-between">
                    <div>
                        <h3 class="text-white mt-3">{{ teamMember.name }}</h3>
                        <h6 class="text-white mb-2">{{ teamMember.position }}</h6>
                        <p>{{ teamMember.description }}</p>
                    </div>
                    <img src="/assets/image/linkImg.png" alt="" class="link img-fluid">
                </div>
            </div>
            <div class="col-3 col-sm-6">
                <div class="imgSec">
                    <img :src="teamMember.image" alt="" class="img-fluid pt-4">
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { onMounted } from "vue";
const props = defineProps({
    teamMember: {
        type: Object,
        required: true,
    },
});

</script>
<style scoped>
.teamMemberCard{
    background-color: #1E35BC;
    border-radius: 20px;
    padding: 1.5em 2em 0;
    margin-top: 30px;
    color: #fff;
    position: relative;
}
.teamMemberCard .row{
    position: relative;
    z-index: 2;
}
.teamMemberCard .blueBg{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: calc(100% - 40px);
    background-color: #111F61;
    border-radius: 20px;
    z-index: 1;
}
.teamMemberCard p{
    font-size: 15px;
}
.teamMemberCard .imgSec{
    height: 100%;
    display: flex;
    align-items: end;
}
.teamMemberCard .imgSec img{
    width: 90%;
    filter: grayscale(100%);
}
.teamMemberCard:hover .imgSec img{
    filter: grayscale(0);
    transition: filter 0.4s ease-in-out;
}
.teamMemberCard .link{
    width: 40%;
    height: 54px;
    object-fit: contain;
    max-width: 150px;
    margin-bottom: 6px;
}
.teamMemberCard .position{
    line-height: 1;
    position: absolute;
    top: 18%;
    right: -4vw;
    font-size: 8vw;
    color: rgb(255, 255, 255, 0.1);
    z-index: 1;
    transform: rotate(-90deg);
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
    .imgSec{
        width: 35%;
        position: absolute;
        right: 0px;
        bottom: 0;
    }
    .imgSec img{
        width: 100%;
    }
}

</style>