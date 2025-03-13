export function getCurrentUser(): number {
  return Number(localStorage.getItem("current_user"));
}


export function getCurrentToken() {
  return localStorage.getItem("current_token");
}