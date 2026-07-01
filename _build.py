# build site script
import glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
gallery = sorted(glob.glob("assets/gallery-*.jpg"))
imgs = "\n".join(f'        <img src="{f}" alt="Foto Da Maino" loading="lazy">' for f in gallery)
with open("index.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pizzeria Ristorante Enoteca da Maino | Conco, Altopiano di Asiago</title>
  <meta name="description" content="Pizzeria Ristorante Enoteca da Maino sull'Altopiano di Asiago. Tradizione montana, pizza artigianale, vini selezionati dal 2005.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>\U0001f355</text></svg>">
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:Georgia,'Times New Roman',serif;color:#2c2c2c;background:#faf8f4;line-height:1.6}
    img{max-width:100%;height:auto;display:block}
    a{color:inherit;text-decoration:none}
    :root{--gold:#c8a43a;--gold-dark:#a8882e;--wood:#5c3d2e;--green:#4a7c3f;--bg:#faf8f4;--bg-alt:#f3efe8;--text-light:#666}
    h1,h2{font-weight:700}
    h2{font-size:2rem;text-align:center;margin-bottom:2.5rem;position:relative;padding-bottom:.75rem}
    h2::after{content:'';position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:60px;height:3px;background:var(--gold);border-radius:2px}
    .section{padding:4rem 1.5rem;max-width:1100px;margin:0 auto}
    .section-alt{background:var(--bg-alt)}
    .btn{display:inline-block;padding:.85rem 2rem;border-radius:50px;font-weight:600;font-size:1rem;cursor:pointer;transition:.2s;border:2px solid transparent;font-family:Georgia,serif}
    .btn-gold{background:var(--gold);color:#fff}
    .btn-gold:hover{background:var(--gold-dark);transform:translateY(-2px)}
    .btn-outline{border-color:#fff;color:#fff;background:transparent}
    .btn-outline:hover{background:rgba(255,255,255,.15)}
    .hero{min-height:85vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:linear-gradient(rgba(30,20,10,.6),rgba(30,20,10,.6)),url('assets/hero-bg.jpg') center/cover fixed;color:#fff;padding:2rem 1rem;position:relative}
    .hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:80px;background:linear-gradient(transparent,var(--bg))}
    .hero-logo{max-width:140px;margin-bottom:1.5rem;border-radius:50%;border:3px solid var(--gold)}
    .hero h1{font-size:clamp(1.8rem,5vw,3.2rem);letter-spacing:1px}
    .hero p{font-size:clamp(1rem,2.5vw,1.3rem);max-width:500px;margin:.75rem auto 2rem;opacity:.9;font-style:italic}
    .hero-btns{display:flex;gap:1rem;flex-wrap:wrap;justify-content:center}
    nav{position:sticky;top:0;z-index:100;background:rgba(44,44,44,.97);backdrop-filter:blur(8px);padding:.75rem 1.5rem;display:flex;justify-content:center;gap:.75rem;flex-wrap:wrap;border-bottom:2px solid var(--gold)}
    nav a{color:#eee;font-size:.85rem;font-weight:600;padding:.4rem .85rem;border-radius:6px;transition:.2s;text-transform:uppercase;letter-spacing:.5px}
    nav a:hover{background:var(--gold);color:#2c2c2c}
    .about-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}
    .about-grid img{border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,.1)}
    .about-text p+p{margin-top:1rem}
    .about-text strong{color:var(--gold-dark)}
    .menu-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem}
    .menu-card{background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.08);transition:transform .2s;border-left:4px solid var(--gold)}
    .menu-card:hover{transform:translateY(-4px)}
    .menu-card-body{padding:1.5rem}
    .menu-card h3{font-size:1.15rem;margin-bottom:.4rem;color:var(--wood)}
    .menu-card .price{color:var(--gold);font-weight:700;font-size:1.2rem}
    .menu-card p{font-size:.9rem;color:var(--text-light);margin:.5rem 0 0}
    .carousel-wrap{position:relative;max-width:900px;margin:0 auto}
    .carousel-viewport{overflow:hidden;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,.12)}
    .carousel-track{display:flex;transition:transform .5s ease}
    .carousel-track img{min-width:100%;height:500px;object-fit:cover}
    .carousel-btn{position:absolute;top:50%;transform:translateY(-50%);z-index:10;background:rgba(0,0,0,.5);color:#fff;border:none;width:44px;height:44px;border-radius:50%;font-size:1.5rem;cursor:pointer;transition:.2s;display:flex;align-items:center;justify-content:center}
    .carousel-btn:hover{background:var(--gold);color:#2c2c2c}
    .carousel-prev{left:10px}
    .carousel-next{right:10px}
    .carousel-dots{display:flex;justify-content:center;gap:.5rem;margin-top:1rem}
    .carousel-dot{width:10px;height:10px;border-radius:50%;background:#ccc;border:none;cursor:pointer;transition:.2s}
    .carousel-dot.active{background:var(--gold);transform:scale(1.3)}
    .reviews-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem}
    .review-card{background:#fff;padding:1.5rem;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.06);position:relative;border-top:3px solid var(--gold)}
    .review-card::before{content:'\00AB';font-size:3rem;color:var(--gold);opacity:.3;position:absolute;top:.5rem;left:1rem;line-height:1}
    .review-card .stars{color:#f5b342;font-size:1.1rem;margin-bottom:.5rem}
    .review-card p{font-size:.95rem;font-style:italic;margin-bottom:.5rem}
    .review-card cite{font-size:.85rem;color:#888;font-style:normal}
    .reviews-link{text-align:center;margin-top:2rem}
    .reviews-link a{color:var(--gold);font-weight:600}
    .reviews-link a:hover{text-decoration:underline}
    .map-container{border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.1)}
    .map-container iframe{width:100%;height:400px;border:0}
    .info-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem}
    .info-grid div{padding:1.25rem;background:#fff;border-radius:10px;border-left:3px solid #4a7c3f}
    .info-grid h3{font-size:1rem;margin-bottom:.5rem;color:var(--gold)}
    .info-grid p{font-size:.9rem;color:#555}
    .cta-bar{position:fixed;bottom:0;left:0;right:0;z-index:300;background:rgba(44,44,44,.98);backdrop-filter:blur(8px);padding:.75rem 1.5rem;display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;border-top:2px solid var(--gold)}
    .cta-bar p{color:#fff;font-size:1rem;font-weight:600}
    .cta-bar .btn{padding:.65rem 1.5rem;font-size:.95rem}
    .cta-bar .btn:hover{transform:translateY(-1px)}
    body{padding-bottom:70px}
    footer{background:#2c2c2c;color:#ccc;text-align:center;padding:2.5rem 1.5rem 1.5rem}
    footer .social{margin-bottom:1rem}
    footer .social a{display:inline-block;padding:.5rem 1rem;border:1px solid #555;border-radius:50px;color:#ddd;font-size:.9rem;transition:.2s}
    footer .social a:hover{background:var(--gold);border-color:var(--gold);color:#2c2c2c}
    footer p{font-size:.85rem}
    footer .credits{margin-top:.75rem;opacity:.6;font-size:.8rem}
    @media(max-width:768px){.about-grid,.info-grid{grid-template-columns:1fr}.hero{min-height:70vh}.carousel-track img{height:300px}.cta-bar p{font-size:.85rem}.cta-bar .btn{padding:.55rem 1rem;font-size:.85rem}}
    @media(max-width:480px){.section{padding:2.5rem 1rem}h2{font-size:1.6rem}.hero-btns{flex-direction:column;align-items:center}.btn{width:100%;max-width:260px;text-align:center}.cta-bar{flex-direction:column;text-align:center;padding:.6rem 1rem}.cta-bar .btn{width:100%}body{padding-bottom:100px}}
  </style>
</head>
<body>
