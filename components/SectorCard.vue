<template>

    <div class="sectorCard">
        <NuxtLink to="#">
            <div class="h-100 d-flex flex-column justify-content-between">
                <div>
                    <img :src="sector.image" class="sectorImg" alt="" />
                    <h5 class="themeText">{{ sector.title }}</h5>
                    <p>{{ sector.description }}</p>
                    <!-- <h5>Key Services:</h5>
                    <ul>
                        <li v-for="service in sector.services" :key="service">{{ service }}</li>
                    </ul> -->
                </div>
                <a href="#" class="link">
                    Contact us
                    <span class="material-symbols-outlined">arrow_forward_ios</span>
                </a>
            </div>
        </NuxtLink>
    </div>

</template>

<script setup>
import { onMounted } from "vue";
const props = defineProps({
    sector: {
        type: Object,
        required: true,
    },
});

</script>
<style scoped>
.sectorCard a{
    text-decoration: none;
    color: black;
}
.sectorCard{
    border: 1px solid #e1e1e1;
    padding: 1.4em;
    border-radius: 10px;
    margin-bottom: 20px;
    height: calc(100% - 20px);
}
.sectorCard:hover{
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s ease-in-out;
}
.sectorCard .sectorImg{
    width: 100%;
    border-radius: 10px;
    margin-bottom: 20px;
    aspect-ratio: 470/360;
    object-fit: cover;
}
.sectorCard p{
    color: #444;
    font-size: 15px;
}
.sectorCard .link{
    width: 100%;
    background-color: #111F61;
    border-radius: 50px;
    padding: 10px 15px;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
}
.sectorCard .link span{
    font-size: 16px;
    margin-left: 5px;
    
}
.sectorCard ul{
    padding-left: 20px;
    list-style-type: none;
}
.sectorCard ul li{
    line-height: 1.3;
    color: #444;
    font-size: 15px;
}
.sectorCard ul li::before{
    content: "•";
    color: #444;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
    font-size: 20px;
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
    .sectorCard{
        margin: 0 5px !important;
    }
}

</style>