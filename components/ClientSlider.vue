<template>
    
    <div class="sliderBg">
        <div class="container-fluid px-0 py-2">
            <div class="client-slider">
                <div v-for="(client, index) in clients" :key="index" class="clientSlide">
                    <img :src="client.image" alt="" />
                </div>
            </div>
        </div>
    </div>

</template>
<script setup>
import { onMounted } from "vue";

const clients = [
    { image: '/assets/image/client1.png' },
    { image: '/assets/image/client2.png' },
    { image: '/assets/image/client3.png' },
    { image: '/assets/image/client4.png' },
    { image: '/assets/image/client1.png' },
    { image: '/assets/image/client2.png' },
    { image: '/assets/image/client3.png' },
    { image: '/assets/image/client4.png' },
];

onMounted(() => {
    // Singleton loader for jQuery + Slick to avoid duplicate loads across pages
    const ensureSlick = () => new Promise((resolve, reject) => {
        if (window.__slick_loaded) return resolve();
        if (window.__slick_loading) {
            // poll until loaded
            const t = setInterval(() => {
                if (window.__slick_loaded) {
                    clearInterval(t);
                    resolve();
                }
            }, 50);
            // timeout after 10s
            setTimeout(() => { clearInterval(t); if (!window.__slick_loaded) reject(new Error('Slick load timeout')); }, 10000);
            return;
        }

        window.__slick_loading = true;

        // add CSS once
        if (!document.querySelector('link[data-slick-css]')) {
            const l1 = document.createElement('link');
            l1.rel = 'stylesheet';
            l1.href = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css';
            l1.setAttribute('data-slick-css', '1');
            document.head.appendChild(l1);
            const l2 = document.createElement('link');
            l2.rel = 'stylesheet';
            l2.href = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.min.css';
            l2.setAttribute('data-slick-css', '1');
            document.head.appendChild(l2);
        }

        const loadScript = (src) => new Promise((res, rej) => {
            // avoid adding duplicate script tags
            if (document.querySelector(`script[src="${src}"]`)) return res();
            const s = document.createElement('script');
            s.src = src;
            s.async = false;
            s.onload = () => res();
            s.onerror = () => rej(new Error('Failed to load ' + src));
            document.head.appendChild(s);
        });

        // Load jQuery first (if not present), then slick
        const jquerySrc = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js';
        const slickSrc = 'https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js';

        const loadAll = async () => {
            try {
                if (!window.$) await loadScript(jquerySrc);
                // ensure global jQuery is available
                if (!window.$ && window.jQuery) window.$ = window.jQuery;
                await loadScript(slickSrc);
                // tiny delay for plugin attach
                await new Promise(r => setTimeout(r, 50));
                window.__slick_loaded = true;
                window.__slick_loading = false;
                resolve();
            } catch (err) {
                window.__slick_loading = false;
                reject(err);
            }
        };
        loadAll();
    });

    const initSlider = () => {
        try {
            const $ = window.$;
            if (!$) return;
            const $slider = $('.client-slider');
            if (!$slider.length) return;
            if ($slider.hasClass('slick-initialized')) {
                $slider.slick('unslick');
            }
            $slider.slick({
                infinite: true,
                slidesToShow: 6,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed: 0,
                speed: 8000,
                pauseOnHover: false,
                pauseOnFocus: false,
                pauseOnDotsHover: false,
                arrows: false,
                draggable: false,
                swipe: false,
                touchMove: false,
                focusOnSelect: false,
                cssEase: 'linear',
                responsive: [
                    { breakpoint: 2600, settings: { slidesToShow: 6, slidesToScroll: 1 } },
                    { breakpoint: 1440, settings: { slidesToShow: 5, slidesToScroll: 1 } },
                    { breakpoint: 1024, settings: { slidesToShow: 4, slidesToScroll: 1 } },
                    { breakpoint: 768, settings: { slidesToShow: 3, slidesToScroll: 1 } },
                    { breakpoint: 576, settings: { slidesToShow: 2, slidesToScroll: 1 } },
                ]
            });
        } catch (e) {
            console.warn('initSlider error', e);
        }
    };

    // Ensure Slick is loaded then initialize. Works across SPA navigation.
    ensureSlick().then(() => {
        // small delay to ensure DOM is attached
        requestAnimationFrame(() => initSlider());
        // also init after a short timeout to handle race cases
        setTimeout(initSlider, 120);
    }).catch(err => console.error('Failed to ensure slick', err));

});


</script>
<style scoped>
.sliderBg {
    background-color: #FFE8C5;
}

.client-slider {
    width: 100%;
    margin: 0 auto;
}

.client-slider .slick-list {
    overflow: hidden;
}

.client-slider .slick-slide {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* keep Slick's own track/slide layout intact; avoid forcing flex/float overrides */

.clientSlide {
    padding: 0 8px;
    box-sizing: border-box;
    width: 160px;
    flex: 0 0 auto;
}

.clientSlide img {
    max-width: 100%;
    max-height: 80px;
    object-fit: contain;
    display: block;
    margin: 0 auto;
}

@media only screen and (max-width:1440px) {
    
}
@media only screen and (max-width:1280px) {
    
}
@media only screen and (max-width:1080px) {
    
}
@media only screen and (max-width:780px) {
    
}
@media only screen and (max-width:578px) {
    
}
</style>