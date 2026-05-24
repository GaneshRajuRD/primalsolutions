<template>
                <div class="teamMemberCard" @click="open" role="button">
                    <div class="card">
                        <img :src="teamMember.image" :alt="`Photo of ${teamMember.name}`" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title">{{ teamMember.name }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ teamMember.position }}</h6>
                            <p class="card-text" v-if="teamMember.description">{{ teamMember.description }}</p>
                            <button
                                class="btn btn-link p-0 read-more-btn"
                                type="button"
                                @click.stop="open"
                            >
                                Read more
                            </button>
                            <a :href="`tel:${teamMember.contact}`" class="card-text contact" v-if="teamMember.contact" @click.stop>{{ teamMember.contact }}</a>
                        </div>
                    </div>
                </div>
            </template>

            <script setup>
            const props = defineProps({
                teamMember: {
                    type: Object,
                    required: true,
                },
            });
            const emit = defineEmits(["open"]);
            const open = () => emit('open', props.teamMember);

            </script>

<style scoped>
.teamMemberCard {
    margin-bottom: 20px;
    height: 100%;
}

.card {
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    height: 100%;
}

.card-img-top {
    width: 100%;
    aspect-ratio: 330/387;
    object-fit: cover;
}

.card-body {
    padding: 15px;
}

.card-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}

.card-subtitle {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}

.card-text {
    font-size: 14px;
    color: #333;
}

.contact {
    text-decoration: none;
    font-weight: bold;
    color: #007bff;
}

.teamMemberCard .read-more-btn {
    position: absolute;
    right: 16px;
    bottom: 14px;
    margin: 0;
    background-color: #111F61;
    color: #fff;
    font-size: 13px;
    font-weight: 500;
    border-radius: 50px;
    padding: 4px 12px !important;
    text-decoration: none;
    line-height: 1.4;
    border: 1px solid #111F61;
    transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
}
.teamMemberCard .read-more-btn:hover,
.teamMemberCard .read-more-btn:focus {
    background-color: #fff;
    color: #111F61;
    text-decoration: none;
    transform: translateX(2px);
    box-shadow: 0 2px 6px rgba(17, 31, 97, 0.18);
}

/* Ensure absolute positioning works */
.teamMemberCard .card-body {
    position: relative;
    padding-bottom: 26px;
}
</style>