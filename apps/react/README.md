# Blog Técnico - João Developer

Um blog moderno inspirado no Reddit para compartilhamento de relatos técnicos, projetos, decisões de arquitetura e aprendizados de desenvolvimento.

## Objetivo

Criar um espaço onde um desenvolvedor documenta suas experiências práticas (como um diário técnico), enquanto leitores podem comentar, questionar e aprender com cada relato.

## Tecnologias Utilizadas

- **React 18** - Biblioteca principal
- **TypeScript** - Tipagem estática
- **Vite** - Build tool
- **TailwindCSS** - Estilização
- **Lucide React** - Ícones

## Estrutura do Projeto

```
src/
├── components/          # Componentes reutilizáveis
│   ├── Navbar.tsx     # Barra de navegação do autor
│   ├── Post.tsx       # Componente de post técnico
│   └── Sidebar.tsx    # Sidebar com categorias técnicas
├── data/              # Dados mockados
│   ├── categories.ts  # Categorias técnicas
│   └── posts.ts      # Posts técnicos de exemplo
├── pages/             # Páginas da aplicação
│   └── Home.tsx      # Página principal com feed
├── styles/            # Estilos globais
├── utils/             # Utilitários
├── hooks/             # Hooks customizados
├── App.tsx           # Componente principal
├── main.tsx          # Ponto de entrada
└── index.css         # Estilos globais
```

## Categorias Técnicas

- Frontend 
- Backend 
- DevOps 
- Arquitetura de Software 
- Bugs e Debugging 
- Performance 
- Projetos Reais 
- Aprendizados 
- Erros e Falhas 
- Boas Práticas 

## Funcionalidades Implementadas

### Layout de Autor Único
- Navbar personalizada com informações do autor
- Layout em 3 colunas otimizado para conteúdo técnico
- Design minimalista focado em legibilidade

### Posts Técnicos
- Posts com metadados técnicos (tempo de leitura, dificuldade)
- Sistema de votação para avaliação de conteúdo
- Tags técnicas para organização por tecnologia
- Alertas para perguntas não respondidas

### Categorias Especializadas
- 10 categorias focadas em desenvolvimento
- Filtragem por área técnica
- Sidebar com navegação especializada

### Sistema de Interação
- Foco em comentários e perguntas
- Threads aninhados estilo Reddit
- Destaque para perguntas não respondidas
- Indicador visual de autor

### Ordenação Relevante
- Posts "Recentes" (por data)
- Posts "Populares" (por votos)
- Posts "Discutidos" (por comentários)

### Conteúdo Auxiliar
- Perfil do autor na sidebar
- Posts mais discutidos
- Tecnologias populares
- Perguntas em aberto

### Responsividade Completa
- Layout adaptado para todos dispositivos
- Sidebar mobile colapsável
- Otimização para leitura técnica

## Dados Técnicos:
- 5 posts técnicos detalhados com exemplos de código
- Estrutura completa de categorias de desenvolvimento
- Sistema de comentários com perguntas e respostas
- Metadados técnicos (nível de dificuldade, tempo de leitura)

## Próximos Passos:
- Página de post individual com renderização Markdown
- Sistema de comentários em tempo real
- Busca avançada por tecnologias e temas
- Dark mode para leitura noturna
- Integração com CMS para gestão de conteúdo

## Diferenciais:

- **Foco em conteúdo técnico**: Relatos práticos do dia a dia
- **Formato educativo**: Cada post inclui contexto, problema, solução e aprendizado
- **Interação direta**: Leitores podem fazer perguntas e receber respostas do autor
- **Metadados úteis**: Tempo de leitura e nível de dificuldade para cada post
- **Organização por tecnologia**: Tags e categorias específicas para desenvolvimento

## Como Executar

1. Instale as dependências:
```bash
npm install
```

2. Inicie o servidor de desenvolvimento:
```bash
npm run dev
```

3. Abra http://localhost:3000 no navegador

## 📦 Próximos Passos

### 🔄 Funcionalidades a Implementar

- [ ] Sistema de rotas com React Router
- [ ] Página de post individual com comentários
- [ ] Formulário para criação de novos posts
- [ ] Sistema de comentários aninhados
- [ ] Modo anônimo para postagens
- [ ] Busca e filtragem avançada
- [ ] Dark mode
- [ ] Sistema de autenticação
- [ ] Backend com Firebase/Supabase

### 🎨 Melhorias de UI/UX

- [ ] Animações e transições
- [ ] Loading states
- [ ] Tratamento de erros
- [ ] Accessibility improvements
- [ ] Performance optimizations

## 📄 Licença

MIT License
