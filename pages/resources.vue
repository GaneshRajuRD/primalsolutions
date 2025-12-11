<template>
    <div class="body">
        <Header />

        <div class="resourcesBnr">
            <div class="container">
                <div class="content text-center">
                    <h1 class="fw-bold">Resources</h1>
                    <p>
                        Explore exciting opportunities and grow your career in property management with us
                    </p>
                </div>
            </div>
        </div>

        <div class="container py-5 ">
            <div class="resource-tabs nav nav-tabs" role="tablist">
                <button
                    class="tab-btn nav-link active" data-bs-toggle="tab" data-bs-target="#Blogs" type="button"
                    role="tab" aria-controls="nav-Blogs" aria-selected="true" id="nav-Blogs-tab">
                    Blogs
                </button>
                <button class="tab-btn nav-link"data-bs-toggle="tab" data-bs-target="#CaseStudies"
                    type="button" role="tab" aria-controls="nav-CaseStudies" aria-selected="false"
                    id="nav-CaseStudies-tab">
                    Case Studies
                </button>
                <button class="tab-btn nav-link" data-bs-toggle="tab" data-bs-target="#Gallery"
                type="button" role="tab" aria-controls="nav-Gallery" aria-selected="false"
                id="nav-Gallery-tab">
                    Gallery
                </button>
            </div>

            <div class="tab-content">
                <div class="tab-pane fade show active" id="Blogs" role="tabpanel" aria-labelledby="nav-Blogs-tab" >
                    <h2 class="fw-light mb-4 pt-5">Latest <span class="fw-bold">Blogs</span></h2>
                    <div class="blogCard2" v-for="blog in blogs.slice(0,1)">
                        <div class="row">
                            <div class="col-sm-7 pe-lg-5">
                                <img :src="blog.image" class="blogImg w-100 img-fluid" alt="" />
                            </div>
                            <div class="col-sm-5">
                                <h3>{{ blog.title }}</h3>
                                <p>{{ blog.description }}</p>
                                <a href="#" class="link fw-bold">
                                    <img src="/assets/image/arrowImg.png" alt="arrow-right" />
                                    READ MORE
                                </a>
                            </div>
                        </div>
                    </div>

                    <h2 class="fw-light mb-4 mt-5 pt-lg-4">Browse All <span class="fw-bold">Blogs</span></h2>
                    <div class="row">
                        <div class="col-sm-6" v-for="blog in blogs">
                            <BlogCard :blog="blog" />
                        </div>
                    </div>

                </div>
                <div class="tab-pane fade" id="CaseStudies" role="tabpanel" aria-labelledby="nav-CaseStudies-tab" >
                    <div class="row py-5">
                        <div class="col-sm-6" v-for="caseStudy in caseStudies">
                            <CaseStudyCard :caseStudy="caseStudy" />
                        </div>
                    </div>
                </div>
                <div class="tab-pane fade" id="Gallery" role="tabpanel" aria-labelledby="nav-Gallery-tab" >
                    <div class="row py-5">
                        <div class="col-sm-6 col-lg-4" v-for="gallery in galleryImages">
                            <GalleryCard :gallery="gallery" />
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <Footer />

        
    </div>
</template>
<script setup>
import { onMounted, ref, watch } from "vue";
import { useRoute } from 'vue-router';

const blogs = ref([
    {
        title: 'Sustainable Practices Reducing Waste in Industrial Production',
        description: 'Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking overpass is important',
        image: '/assets/image/blogImg1.webp',
        url: 'sustainable-practices-reducing-waste-in-industrial-production'
    },
    {
        title: 'Advanced Robotics Revolutionizing Industrial Workflows',
        image: '/assets/image/blogImg2.webp',
        url: 'advanced-robotics-revolutionizing-industrial-workflows'
    },
]);
const caseStudies = ref([
    {
        title: 'Transforming Production Efficiency for a Leading Sheet Metal Manufacturer in Hosur',
        image: '/assets/image/caseStudyImg1.webp',
        readtime: '8 min read',
        date: 'Nov 15, 2025',
        url: 'case-study'
    },
    {
        title: 'Transforming Production Efficiency for a Leading Sheet Metal Manufacturer in Hosur',
        image: '/assets/image/caseStudyImg1.webp',
        readtime: '8 min read',
        date: 'Nov 15, 2025',
        url: 'case-study'
    },
]);

const galleryImages = ref([
    {
        image: '/assets/image/blogImg2.webp'
    },
    {
        image: '/assets/image/blogImg1.webp'
    },
    {
        image: '/assets/image/caseStudyImg1.webp'
    },
]);

const route = useRoute();

function activateTabFromHash(hash) {
    if (!hash) return;
    const target = hash.startsWith('#') ? hash : `#${hash}`;
    const btn = document.querySelector(`.resource-tabs [data-bs-target="${target}"]`);
    if (btn) {
        try {
            btn.click();
        } catch (e) {
            btn.dispatchEvent(new Event('click'));
        }
        // fallback: if bootstrap JS not available, toggle classes manually
        setTimeout(() => {
            const activeBtn = document.querySelector('.resource-tabs .nav-link.active');
            if (!btn.classList.contains('active')) {
                if (activeBtn) activeBtn.classList.remove('active');
                btn.classList.add('active');
                const activePane = document.querySelector('.tab-content .tab-pane.show.active');
                if (activePane) {
                    activePane.classList.remove('show', 'active');
                }
                const pane = document.querySelector(target);
                if (pane) {
                    pane.classList.add('show', 'active');
                }
            }
        }, 60);

        const el = document.querySelector(target);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

onMounted(() => {
    activateTabFromHash(route.hash);
});

watch(() => route.hash, (h) => {
    activateTabFromHash(h);
});

</script>
<style scoped>
.body{
    background-color: #F5F5F5;
}
.resourcesBnr {
    position: relative;
    background-image: linear-gradient(to right,rgb(0, 0, 0),rgb(0, 0, 0,0.19)),url('/assets/image/aboutUsBnr.webp');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
}
.resourcesBnr h1{
    color: #fff;
}
.resourcesBnr .content {
    height: 90vh;
    display: flex;
    justify-content: center;
    color: #fff;
    flex-direction: column;
    position: relative;
    z-index: 1;
}
.resourcesBnr .content h1 {
    font-size: 60px;
}

.resource-tabs{
    display: flex;
    justify-content: center;
    gap: 20px;
    border: none;
}
.resource-tabs button{
    width: 18%;
    padding: 14px 3em;
    font-weight: 500;
    color: #000;
    border: 1px solid #e1e1e1;
    background-color: #fff;
    border-radius: 40px;
}
.resource-tabs button.active{
    background-color: #111F61;
    color: #fff;
    border: 1px solid #111F61;
}
.blogCard2 {
    margin-bottom: 30px;
}
.blogCard2 .blogImg{
    border-radius: 20px;
}
.blogCard2 p{
    line-height: 1.8;
}
.blogCard2 .link{
    text-decoration: none;
    color: #222;
    width: max-content;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
}
.blogCard2 .link img{
    background-color: #132162;
    height: 30px;
    width: 30px;
    padding: 5px;
    border-radius: 8px;
    aspect-ratio: 1/1;
    object-fit: contain;
}


@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    .resourcesBnr .content h1 {
        font-size: 50px;
    }
}
@media only screen and (max-width:1080px) {
    .resourcesBnr .content h1 {
        font-size: 44px;
    }
    .resource-tabs button{
        width: 27%;
        padding: 14px 1em;
    }
}
@media only screen and (max-width:830px) {
    .resourcesBnr .content h1 {
        font-size: 40px;
    }
}
@media only screen and (max-width:578px) {
    .resource-tabs {
        flex-wrap: wrap;
        gap: 12px;
    }
    .resource-tabs button{
        width: 31%;
        padding: 10px;
        font-size: 14px;
    }
}
</style>