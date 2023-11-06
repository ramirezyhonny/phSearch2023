//dates for select address
const provincesCountry = {
    Espana: ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza"],
    Francia: ["París", "Marsella", "Lyon", "Toulouse", "Niza"],
    Italia: ["Roma", "Milán", "Nápoles", "Florencia", "Venecia"],
    Alemania: ["Berlín", "Múnich", "Hamburgo", "Colonia", "Frankfurt"],
    ReinoUnido: ["Londres", "Manchester", "Liverpool", "Glasgow", "Edimburgo"],
    EstadosUnidos: ["Nueva York", "Los Ángeles", "Chicago", "Miami", "San Francisco"],
    Canada: ["Toronto", "Montreal", "Vancouver", "Ottawa", "Calgary"],
    Australia: ["Sídney", "Melbourne", "Brisbane", "Perth", "Adelaida"],
    Japon: ["Tokio", "Osaka", "Kioto", "Hiroshima", "Nagoya"],
    China: ["Pekín", "Shanghái", "Cantón", "Chengdú", "Wuhan"],
    India: ["Nueva Delhi", "Bombay", "Bangalore", "Chennai", "Kolkata"],
    Mexico: ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Tijuana"],
    Argentina: ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Tucumán"],
    Brasil: ["São Paulo", "Río de Janeiro", "Brasilia", "Salvador", "Belo Horizonte"],
    Chile: ["Santiago", "Valparaíso", "Concepción", "Antofagasta", "Viña del Mar"],
    Peru: ["Lima", "Arequipa", "Trujillo", "Cusco", "Piura"],
    Colombia: ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"],
    Ecuador: ["Quito", "Guayaquil", "Cuenca", "Ambato", "Machala"],
    Venezuela: ["Caracas", "Maracaibo", "Valencia", "Barquisimeto", "Maracay"],
    Uruguay: ["Montevideo", "Salto", "Paysandú", "Maldonado", "Rivera"],
    Paraguay: ["Asunción", "Ciudad del Este", "Encarnación", "San Lorenzo", "Lambaré"],
    Bolivia: ["La Paz", "Santa Cruz", "Cochabamba", "Sucre", "Tarija"],
    Paraguay: ["Asunción", "Ciudad del Este", "Encarnación", "San Lorenzo", "Lambaré"],
    CostaRica: ["San José", "Alajuela", "Heredia", "Liberia", "Puntarenas"],
    Guatemala: ["Ciudad de Guatemala", "Quetzaltenango", "Escuintla", "Chimaltenango", "Cobán"],
    Honduras: ["Tegucigalpa", "San Pedro Sula", "La Ceiba", "Choluteca", "Comayagua"],
    Nicaragua: ["Managua", "León", "Granada", "Masaya", "Chinandega"],
    Panama: ["Ciudad de Panamá", "Colón", "David", "Santiago", "Chitré"],
    Cuba: ["La Habana", "Santiago de Cuba", "Camagüey", "Holguín", "Santa Clara"],
    RepublicaDominicana: ["Santo Domingo", "Santiago", "Santo Domingo Este", "San Pedro de Macorís", "La Romana"]
};
function loadProvinces() {
    const countrySelect = document.getElementById("id_country");
    const provinceSelect = document.getElementById("id_province");
    const selectedCountry = countrySelect.value;
    // Borra las opciones anteriores
    provinceSelect.innerHTML = "<option value=''>Select your province</option>";

    if (selectedCountry in provincesCountry) {
        const provinces = provincesCountry[selectedCountry];
        for (const province of provinces) {
            const option = document.createElement("option");
            option.value = province;
            option.text = province;
            provinceSelect.appendChild(option);
        }
    }
}




