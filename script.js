// Pet Data
const pets = [
    { id: 1, name: "Bella", type: "Dog", age: 2, image: "C:\Users\lenovo\Desktop\fsd proj", description: "Friendly and playful!" },
    { id: 2, name: "Max", type: "Cat", age: 3, image: "C:\Users\lenovo\Desktop\fsd proj", description: "Loves to nap in the sun." },
    { id: 3, name: "Charlie", type: "Rabbit", age: 1, image: "C:\Users\lenovo\Desktop\fsd proj", description: "Small and adorable." },
];

// Load Pets Dynamically
const petsContainer = document.getElementById('pets-container');

function loadPets() {
    petsContainer.innerHTML = "";
    pets.forEach(pet => {
        const petCard = document.createElement('div');
        petCard.classList.add('pet-card');
        petCard.innerHTML = `
            <img src="${pet.image}" alt="${pet.name}">
            <h3>${pet.name}</h3>
            <p>${pet.type} | Age: ${pet.age}</p>
            <button class="adopt-btn" onclick="viewPetDetails(${pet.id})">View Details</button>
        `;
        petsContainer.appendChild(petCard);
    });
}

// View Pet Details
const modal = document.getElementById('modal');
const petDetails = document.getElementById('pet-details');
const closeBtn = document.getElementById('close-btn');

function viewPetDetails(id) {
    const pet = pets.find(p => p.id === id);
    petDetails.innerHTML = `
        <h2>${pet.name}</h2>
        <img src="${pet.image}" alt="${pet.name}" style="max-width: 100%; border-radius: 8px;">
        <p><strong>Type:</strong> ${pet.type}</p>
        <p><strong>Age:</strong> ${pet.age}</p>
        <p>${pet.description}</p>
    `;
    modal.classList.remove('hidden');salkcnsakjbskajbd
}

// Close Modal
closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
});

// Load pets on page load
window.onload = () => {
    loadPets(); // Only load pets; do not manipulate modal visibility
};
