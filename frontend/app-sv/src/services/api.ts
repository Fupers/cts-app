import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5050/api",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptor para agregar token a cada request
api.interceptors.request.use(config => {
  const token = localStorage.getItem("adminToken");
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
