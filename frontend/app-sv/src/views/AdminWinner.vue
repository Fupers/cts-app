<template>
  <div class="min-h-screen bg-sky-50">
    <AdminNavbar />

    <div class="p-8">
      <h1 class="text-2xl font-bold mb-4 text-sky-700">Sorteo de Ganador</h1>

      <button
        @click="drawWinner"
        class="bg-sky-500 text-white py-2 px-4 rounded hover:bg-sky-600"
      >
        Generar Ganador
      </button>

      <div v-if="winner" class="mt-4 p-4 bg-yellow-100 rounded">
        <p><strong>Nombre:</strong> {{ winner.name }}</p>
        <p><strong>Email:</strong> {{ winner.email }}</p>

        <button
          @click="notifyWinner"
          class="mt-4 bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600"
        >
          Mandar correo al ganador
        </button>
      </div>

      <div v-if="message" class="mt-4 p-4 rounded"
           :class="messageType === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import api from '../services/api'
import { ref } from 'vue'
import AdminNavbar from '../components/AdminNavbar.vue'

export default {
  components: { AdminNavbar },
  setup() {
    const winner = ref<any>(null)
    const message = ref('')
    const messageType = ref<'success' | 'error'>('success')

    const drawWinner = async () => {
      try {
        const res = await api.post('/admin/draw_winner/')
        winner.value = res.data
        message.value = `Ganador seleccionado: ${res.data.name}`
        messageType.value = 'success'
      } catch (err: any) {
        message.value = err.response?.data?.error || 'Error al seleccionar ganador'
        messageType.value = 'error'
      }
    }

    const notifyWinner = async () => {
      if (!winner.value) return
      try {
        await api.post('/admin/notify_winner/', {
          winner_id: winner.value.id
        })
        message.value = `Correo enviado a ${winner.value.email}`
        messageType.value = 'success'
      } catch (err: any) {
        message.value = err.response?.data?.error || 'Error al enviar correo'
        messageType.value = 'error'
      }
    }

    return { drawWinner, notifyWinner, winner, message, messageType }
  }
}
</script>
