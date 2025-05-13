:root { --primary: #8B4513; --secondary: #D2691E; --accent: #FF8C00; --light: #FFF8DC; --dark: #3E2723; }

{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
body { background-color: var(--light); color: var(--dark); line-height: 1.6; }

header { background-color: var(--primary); color: white; padding: 20px 0; position: relative; background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/static/images/header-bg.jpg'); background-size: cover; background-position: center; }

.container { width: 90%; max-width: 1200px; margin: 0 auto; padding: 0 20px; }

.logo { font-size: 28px; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; text-align: center; padding: 40px 0; }

.logo span { color: var(--accent); }

.hero { text-align: center; padding: 60px 0; }

.hero h1 { font-size: 48px; margin-bottom: 20px; color: white; }

.hero p { font-size: 20px; margin-bottom: 40px; color: rgba(255, 255, 255, 0.9); max-width: 800px; margin-left: auto; margin-right: auto; }

.btn { display: inline-block; padding: 12px 30px; background-color: var(--accent); color: white; text-decoration: none; border-radius: 30px; font-weight: bold; text-transform: uppercase; transition: all 0.3s ease; margin: 10px; }

.btn:hover { background-color: var(--secondary); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); }

.btn-whatsapp { background-color: #25D366; }

.btn-instagram { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }

section { padding: 80px 0; }

section h2 { text-align: center; font-size: 36px; margin-bottom: 40px; color: var(--primary); position: relative; }

section h2:after { content: ''; display: block; width: 100px; height: 4px; background-color: var(--accent); margin: 15px auto 0; }

.services { background-color: white; }

.services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }

.service-card { background-color: var(--light); padding: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; text-align: center; }

.service-card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15); }

.service-card i { font-size: 48px; color: var(--accent); margin-bottom: 20px; }

.service-card h3 { font-size: 24px; margin-bottom: 15px; color: var(--primary); }

.booking-form { background-color: var(--primary); color: white; padding: 40px; border-radius: 10px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); max-width: 800px; margin: 0 auto; }

.form-group { margin-bottom: 20px; }

.form-group label { display: block; margin-bottom: 8px; font-weight: 600; }

.form-control { width: 100%; padding: 12px 15px; border: none; border-radius: 5px; font-size: 16px; }

textarea.form-control { min-height: 120px; resize: vertical; }

.btn-submit { background-color: var(--accent); border: none; cursor: pointer; width: 100%; font-size: 18px; }

.social-links { text-align: center; margin-top: 40px; }

.social-links a { display: inline-block; width: 60px; height: 60px; background-color: var(--primary); color: white; border-radius: 50%; margin: 0 10px; line-height: 60px; font-size: 24px; transition: all 0.3s ease; }

.social-links a:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); }

.instagram { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }

.whatsapp { background-color: #25D366; }

footer { background-color: var(--dark); color: white; text-align: center; padding: 30px 0; }

footer p { margin: 10px 0; }

@media (max-width: 768px) { .hero h1 { font-size: 36px; }

.hero p {
    font-size: 18px;
}

section {
    padding: 60px 0;
}

.services-grid {
    grid-template-columns: 1fr;
}
}

/* Estilo para o calendário de agendamento */ .calendar-section { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); margin-top: 40px; }

.calendar-container { position: relative; padding-bottom: 75%; height: 0; overflow: hidden; border-radius: 10px; }

.calendar-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }

/* Galeria de fotos */ .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 40px; }

.gallery-item { border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; position: relative; }

.gallery-item:hover { transform: scale(1.03); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }

.gallery-item img { width: 100%; height: 250px; object-fit: cover; display: block; }

.gallery-item .caption { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0, 0, 0, 0.7); color: white; padding: 10px; font-size: 14px; opacity: 0; transition: opacity 0.3s; }

.gallery-item:hover .caption { opacity: 1; }

/* Estilo para os depoimentos */ .testimonials { background-color: white; }

.testimonial-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }

.testimonial-card { background-color: var(--light); padding: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); position: relative; }

.testimonial-card i.quote { font-size: 30px; color: var(--accent); opacity: 0.2; position: absolute; top: 20px; left: 20px; }

.testimonial-text { font-style: italic; margin-bottom: 20px; }

.testimonial-author { font-weight: bold; color: var(--primary); }

/* Estilos para o modal de sucesso */ .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.7); overflow: auto; }

.modal-content { background-color: white; margin: 15% auto; padding: 30px; border-radius: 10px; width: 80%; max-width: 500px; text-align: center; animation: modalOpen 0.4s; }

.modal-content i { font-size: 60px; color: #4CAF50; margin-bottom: 20px; }

.modal-content h3 { color: var(--primary); margin-bottom: 20px; }

.close-modal { background-color: var(--accent); color: white; border: none; padding: 12px 30px; border-radius: 30px; font-weight: bold; cursor: pointer; transition: all 0.3s ease; }

.close-modal:hover { background-color: var(--secondary); }

@keyframes modalOpen { from {opacity: 0; transform: scale(0.8);} to {opacity: 1; transform: scale(1);} }

/* Estilo para loader */ .loading { text-align: center; padding: 40px; grid-column: 1 / -1; }

.loading i { font-size: 40px; color: var(--accent); margin-bottom: 20px; animation: spin 1s linear infinite; }

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }