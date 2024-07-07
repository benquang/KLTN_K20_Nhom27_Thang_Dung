import { Component } from '@angular/core';

@Component({
  selector: 'app-league',
  templateUrl: './league.component.html',
  styleUrl: './league.component.scss'
})
export class LeagueComponent {


  description = 'Tôi đã hoạt động 2 năm trong lĩnh vực BĐS với sức trẻ'
  + ' căng đầy nhiệt huyết, '
  + 'đã giúp tư vấn thành công nhiều giao dịch BĐS'
  + 'cho khách hàng mua nhà và chủ nhà tại thị trường TP. Hồ Chí Minh.';
cards = [
  {
    imageSrc: '/assets/img/logo/Premier_League_Logo.png',
    title: 'Premier League',
    description: 'Premier League, English professional football (soccer) league established in 1992. The league, which comprises 20 clubs, superseded the first division of the English Football League (EFL) as the top level of football in England.',
  },
  {
    imageSrc: '/assets/img/logo/laliga.png',
    title: 'Laliga',
    description: 'The Liga Nacional de Fútbol Profesional (transl. National Professional Football League), also known as LALIGA (the abbreviation LFP was used until the 2015–16 season), is a sports association responsible for administering the two professional football leagues in Spain, the Primera and Segunda Divisions',
  },
  {
    imageSrc: '/assets/img/logo/seriea.svg',
    title: 'Seria',
    description: "The Serie A, officially known as Serie A TIM for sponsorship reasons, is a professional league competition for football clubs located at the top of the Italian football league system and the winners are awarded the scudetto and the Coppa Campioni d'Italia.",
  },
  {
    imageSrc: '/assets/img/logo/bundesliga.png',
    title: 'Bundesliga',
    description: 'The Introduction of the Bundesliga was the long-debated step of establishing a top-level association football league in Germany in 1963. The new league, the Bundesliga, played its first season in 1963–64 and continues to be the highest league in the country. Its introduction reduced the number of first division teams in Germany from 74 to 16 and finally eliminated the problem of the top-teams having to play uncompetitive teams in regional leagues.',
  },
  {
    imageSrc: '/assets/img/logo/ligue1.png',
    title: 'Ligue 1',
    description: 'Ligue 1, officially known as Ligue 1 Uber Eats for sponsorship reasons, is a French professional league for men`s association football clubs.',
  },
];


}
