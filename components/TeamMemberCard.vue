<template>
                <div class="teamMemberCard" @click="open" role="button">
                    <div class="card">
                        <img :src="teamMember.image" alt="" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title">{{ teamMember.name }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ teamMember.position }}</h6>
                            <p class="card-text" v-if="teamMember.description">{{ teamMember.description }}</p>
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
</style>