import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5050/api",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor para agregar token solo si es admin endpoint
api.interceptors.request.use(config => {
  const token = localStorage.getItem("adminToken");
  
  // Solo agregar Authorization si la URL contiene /admin
  if (token && config.url?.startsWith("/admin") && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export default api;

