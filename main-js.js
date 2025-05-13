document.addEventListener('DOMContentLoaded', function() {
    // Carregar imagens do Instagram
    loadInstagramImages();
    
    // Configurar o formulário de orçamento
    setupBookingForm();
    
    // Configurar a rolagem suave
    setupSmoothScroll();
});

/**
 * Carrega imagens do Instagram via API
 */
function loadInstagramImages() {
    const gallery = document.getElementById('instagram-gallery');
    
    fetch('/api/instagram')
        .then(response => response.json())
        .then(posts => {
            // Remover o loader
            gallery.innerHTML = '';
            
            if (posts.length === 0) {
                // Se não houver posts, carregar dados de fallback
                return fetch('/api/fallback-images')
                    .then(response => response.json());
            }
            
            return posts;
        })
        .then(posts => {
            // Adicionar cada imagem à galeria
            posts.forEach(post => {
                const galleryItem = document.createElement('div');
                galleryItem.className = 'gallery-item';
                
                // Criar imagem
                const img = document.createElement('img');
                img.src = post.display_url || post.url;
                img.alt = 'Foto do Na Lenha com Ferreira';
                img.loading = 'lazy'; // Lazy loading para melhorar performance
                
                // Criar legenda
                const caption = document.createElement('div');
                caption.className = 'caption';
                caption.textContent = truncateText(post.caption || '', 100);
                
                // Adicionar link para abrir Instagram
                const link = document.createElement('a');
                link.href = post.shortcode ? 
                    `https://instagram.com/p/${post.shortcode}` : 
                    'https://instagram.com/nalenhacomferreira';
                link.target = '_blank';
                link.appendChild(img);
                link.appendChild(caption);
                
                galleryItem.appendChild(link);
                gallery.appendChild(galleryItem);
            });
        })
        .catch(error => {
            console.error('Erro ao carregar imagens do Instagram:', error);
            
            // Mostrar mensagem de erro
            gallery.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 30px;">
                    <p>Não foi possível carregar as imagens do Instagram. 
                       <a href="https://instagram.com/nalenhacomferreira" target="_blank">
                         Visite nosso perfil no Instagram
                       </a>
                    </p>
                    <div class="gallery" id="fallback-gallery">
                        <div class="gallery-item">
                            <img src="/static/images/placeholder1.jpg" alt="Prato gourmet">
                        </div>
                        <div class="gallery-item">
                            <img src="/static/images/placeholder2.jpg" alt="Evento corporativo">
                        </div>
                        <div class="gallery-item">
                            <img src="/static/images/placeholder3.jpg" alt="Mesa de jantar">
                        </div>
                        <div class="gallery-item">
                            <img src="/static/images/placeholder4.jpg" alt="Buffet de evento">
                        </div>
                    </div>
                </div>
            `;
        });
}

/**
 * Configura o formulário de orçamento para enviar para WhatsApp
 */
function setupBookingForm() {
    document.getElementById('booking-form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Obter os valores do formulário
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const eventType = document.getElementById('event-type').value;
        const eventDate = document.getElementById('event-date').value;
        const guests = document.getElementById('guests').value;
        const message = document.getElementById('message').value;
        
        // Preparar a mensagem para o WhatsApp
        let whatsappMessage = `*Nova Solicitação de Orçamento*\n\n`;
        whatsappMessage += `*Nome:* ${name}\n`;
        whatsappMessage += `*E-mail:* ${email}\n`;
        whatsappMessage += `*Telefone:* ${phone}\n`;
        whatsappMessage += `*Tipo de Serviço:* ${eventType}\n`;
        
        if (eventDate) {
            whatsappMessage += `*Data:* ${eventDate}\n`;
        }
        
        if (guests) {
            whatsappMessage += `*Nº de Pessoas:* ${guests}\n`;
        }
        
        whatsappMessage += `*Detalhes:* ${message}\n`;
        
        // Codificar a mensagem para URL
        const encodedMessage = encodeURIComponent(whatsappMessage);
        
        // Criar o link do WhatsApp
        const whatsappLink = `https://wa.me/5547999925681?text=${encodedMessage}`;
        
        // Mostrar o modal de sucesso
        document.getElementById('success-modal').style.display = 'block';
        
        // Limpar o formulário
        this.reset();
        
        // Redirecionar para o WhatsApp após 2 segundos
        setTimeout(() => {
            window.open(whatsappLink, '_blank');
        }, 2000);
    });
    
    // Fechar o modal quando o botão de fechar for clicado
    document.querySelector('.close-modal').addEventListener('click', function() {
        document.getElementById('success-modal').style.display = 'none';
    });
    
    // Fechar o modal quando clicado fora dele
    window.addEventListener('click', function(event) {
        const modal = document.getElementById('success-modal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

/**
 * Configura a rolagem suave para links internos
 */
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

/**
 * Função auxiliar para truncar texto
 * @param {string} text - Texto a ser truncado
 * @param {number} maxLength - Comprimento máximo
 * @returns {string} - Texto truncado
 */
function truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
}
