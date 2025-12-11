// nuxt.config.ts or nuxt.config.js

export default defineNuxtConfig({
  ssr: true,
  compatibilityDate: '2025-02-04',

  app: {
    baseURL: "/",       // ensures correct path on custom domain
    cdnURL: "",         // prevents CDN rewrite
    head: {
      title: "Primal Solutions",
      htmlAttrs: { lang: "en" },
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
        { hid: "description", name: "description", content: "nuxt project" }
      ],
      link: [
        { rel: "icon", type: "image/x-icon", href: "/primalFavIcon.png" },
        { rel: "stylesheet", href: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" },
        { rel: "stylesheet", href: "/assets/custom.css" },
        { rel: "stylesheet", href: "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" },
        { rel: "stylesheet", href: "https://cdn.jsdelivr.net/npm/@splidejs/splide@4.0.7/dist/css/splide.min.css" },
        { rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" },
      ],
      script: [
        { src: "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" },
        { src: "https://cdnjs.cloudflare.com/ajax/libs/showdown/1.9.1/showdown.min.js" },
        { src: "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" },
        { src: "https://cdn.jsdelivr.net/npm/@splidejs/splide@4.0.7/dist/js/splide.min.js" },
        { src: "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/js/bootstrap-datepicker.js" }
      ]
    }
  },

  // Generates static hosting-friendly build
  nitro: {
    preset: "static"
  },

  runtimeConfig: {
    public: {
      emailApi: "https://express-js-on-vercel-six-nu-63.vercel.app/api/send-email"
    }
  },

  components: true
});