<!DOCTYPE html> <html lang="pt-BR">

<head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Na Lenha com Ferreira | Personal Chef & Consultoria Gastronômica</title> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"> <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}"> </head>
<body> <header> <div class="container"> <div class="logo">Na Lenha <span>com Ferreira</span></div> <div class="hero">

Gastronomia de Excelência para Eventos e Consultorias
Personal chef especializado em culinária de alta qualidade para eventos corporativos, consultorias gastronômicas e experiências culinárias exclusivas.

<a href="#contato" class="btn">Solicitar Orçamento <a href="https://wa.me/5547999925681" class="btn btn-whatsapp" target="_blank"> <i class="fab fa-whatsapp"> WhatsApp <a href="https://instagram.com/nalenhacomferreira" class="btn btn-instagram" target="_blank"> <i class="fab fa-instagram"> Instagram </div> </div> </header>
<section class="services">
    <div class="container">
        <h2>Nossos Serviços</h2>
        <div class="services-grid">
            <div class="service-card">
                <i class="fas fa-utensils"></i>
                <h3>Eventos Corporativos</h3>
                <p>Serviços gastronômicos personalizados para reuniões, confraternizações, lançamentos e eventos empresariais de todos os portes.</p>
            </div>
            <div class="service-card">
                <i class="fas fa-glass-cheers"></i>
                <h3>Eventos Pessoais</h3>
                <p>Do jantar íntimo às grandes celebrações, criamos experiências gastronômicas memoráveis para seus momentos especiais.</p>
            </div>
            <div class="service-card">
                <i class="fas fa-clipboard-list"></i>
                <h3>Consultoria Gastronômica</h3>
                <p>Desenvolvimento de cardápios personalizados, treinamentos e consultoria completa para o seu negócio ou necessidades pessoais.</p>
            </div>
            <div class="service-card">
                <i class="fas fa-user-friends"></i>
                <h3>Parcerias para Eventos</h3>
                <p>Contamos com uma rede de parceiros de decoração e locais para eventos, oferecendo soluções completas para sua ocasião.</p>
            </div>
            <div class="service-card">
                <i class="fas fa-book-open"></i>
                <h3>Criação de Receitas</h3>
                <p>Desenvolvimento de receitas exclusivas e adaptadas às suas preferências e necessidades dietéticas.</p>
            </div>
            <div class="service-card">
                <i class="fas fa-apple-alt"></i>
                <h3>Cardápio Personalizado</h3>
                <p>Elaboração de cardápios que atendem às suas necessidades nutricionais, restrições alimentares e preferências pessoais.</p>
            </div>
        </div>
    </div>
</section>

<section class="gallery-section">
    <div class="container">
        <h2>Galeria de Criações</h2>
        <div class="gallery" id="instagram-gallery">
            <!-- As imagens do Instagram serão carregadas aqui via JavaScript -->
            <div class="loading">
                <i class="fas fa-spinner fa-spin"></i>
                <p>Carregando imagens do Instagram...</p>
            </div>
        </div>
    </div>
</section>

<section class="testimonials">
    <div class="container">
        <h2>Depoimentos</h2>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <i class="fas fa-quote-left quote"></i>
                <p class="testimonial-text">A consultoria gastronômica do Ferreira transformou completamente o cardápio do nosso restaurante. Os clientes notaram a diferença e as vendas aumentaram em mais de 30%.</p>
                <p class="testimonial-author">- Ana Paula, Proprietária de Restaurante</p>
            </div>
            <div class="testimonial-card">
                <i class="fas fa-quote-left quote"></i>
                <p class="testimonial-text">Contratamos para um evento corporativo e superou todas as expectativas. Profissionalismo impecável e comida de altíssima qualidade. Todos os executivos ficaram impressionados.</p>
                <p class="testimonial-author">- Carlos Silva, Diretor de Marketing</p>
            </div>
            <div class="testimonial-card">
                <i class="fas fa-quote-left quote"></i>
                <p class="testimonial-text">O cardápio personalizado que o chef Ferreira desenvolveu para mim mudou minha relação com a comida. Agora consigo manter uma alimentação saudável sem abrir mão do sabor.</p>
                <p class="testimonial-author">- Mariana Costa, Cliente Particular</p>
            </div>
        </div>
    </div>
</section>

<section id="agendamento">
    <div class="container">
        <h2>Agende uma Consultoria</h2>
        <div class="calendar-section">
            <p style="text-align: center; margin-bottom: 20px;">Selecione uma data e horário disponíveis para agendar sua consultoria ou reunião:</p>
            <div class="calendar-container">
                <!-- Aqui você inserirá o código de incorporação do Google Calendar -->
                <iframe src="https://calendar.google.com/calendar/embed?src=nalenhacomferreira%40gmail.com&ctz=America%2FSao_Paulo" style="border: 0" frameborder="0" scrolling="no"></iframe>
            </div>
        </div>
    </div>
</section>

<section id="contato">
    <div class="container">
        <h2>Solicite um Orçamento</h2>
        <form id="booking-form" class="booking-form">
            <div class="form-group">
                <label for="name">Nome Completo</label>
                <input type="text" id="name" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="phone">Telefone/WhatsApp</label>
                <input type="tel" id="phone" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="event-type">Tipo de Serviço</label>
                <select id="event-type" class="form-control" required>
                    <option value="">Selecione</option>
                    <option value="Evento Corporativo">Evento Corporativo</option>
                    <option value="Evento Pessoal">Evento Pessoal</option>
                    <option value="Consultoria Gastronômica">Consultoria Gastronômica</option>
                    <option value="Cardápio Personalizado">Cardápio Personalizado</option>
                    <option value="Criação de Receitas">Criação de Receitas</option>
                    <option value="Outro">Outro</option>
                </select>
            </div>
            <div class="form-group">
                <label for="event-date">Data do Evento/Consultoria (se aplicável)</label>
                <input type="date" id="event-date" class="form-control">
            </div>
            <div class="form-group">
                <label for="guests">Número de Pessoas (se aplicável)</label>
                <input type="number" id="guests" class="form-control" min="1">
            </div>
            <div class="form-group">
                <label for="message">Detalhes do Pedido</label>
                <textarea id="message" class="form-control" required placeholder="Descreva o que você precisa em detalhes para que possamos preparar um orçamento adequado..."></textarea>
            </div>
            <button type="submit" class="btn btn-submit">Enviar Solicitação</button>
        </form>

        <div class="social-links">
            <a href="https://instagram.com/nalenhacomferreira" class="instagram" target="_blank">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="https://wa.me/5547999925681" class="whatsapp" target="_blank">
                <i class="fab fa-whatsapp"></i>
            </a>
        </div>
    </div>
</section>

<!-- Modal de sucesso -->
<div id="success-modal" class="modal">
    <div class="modal-content">
        <i class="fas fa-check-circle"></i>
        <h3>Mensagem Enviada com Sucesso!</h3>
        <p>Obrigado pelo seu contato. Em breve retornaremos com seu orçamento pelo WhatsApp.</p>
        <button class="close-modal">Fechar</button>
    </div>
</div>

<footer>
    <div class="container">
        <p>&copy; 2025 Na Lenha com Ferreira - Personal Chef & Consultoria Gastronômica</p>
        <p>WhatsApp: <a href="https://wa.me/5547999925681" style="color: #25D366; text-decoration: none;">+55 47 99992-5681</a></p>
        <p>Instagram: <a href="https://instagram.com/nalenhacomferreira" style="color: #E1306C; text-decoration: none;">@nalenhacomferreira</a></p>
        <p>Email: <a href="mailto:nalenhacomferreira@gmail.com" style="color: var(--accent); text-decoration: none;">nalenhacomferreira@gmail.com</a></p>
    </div>
</footer>

<!-- Scripts -->
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body> </html>