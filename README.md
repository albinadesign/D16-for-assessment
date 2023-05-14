Проект "Fan dashboard"

ТЗ:

"Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки."

Реализация:

На главной странице сайта незарегистрированному пользователю дается возможность просмотреть список постов:
В меню пользователю доступны кнопки регистрации или входа в систему

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/61f2ce24-a2d9-40b6-b18f-dd26afca8b5a)

При клике на название поста-объявления незарегистрированный пользователь может прочитать как само объвление, так и отзывы на него

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/c6449042-61bb-40ee-a92c-8f59066b42b1)

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/14d45d4c-053a-4e08-81a4-87593e639028)

Пользователь может вернуться назад, либо кликнув на кнопку "Back", либо на название сайта или кнопку "All posts" на панели меню
Также пользователю предлагается войти в систему, чтобы иметь возможность оставлять комментарии и публиковать свои посты/объявления

Чтобы зарегистрироваться, нужно кликнуть на соответствующую кнопку на панели меню

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/78ce8268-04c0-4472-8f8b-fbaa2aa2d92d)

При регистрации пользователю на указанную электронную почту отправляется 4-знаяный код подтверждения, который нужно ввести на следующей странице, открывающейся автоматически

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/ab876476-dfe0-4a8b-8a9c-118f9f8b1de1)

Если введен неверный код, пользователю предлагается либо попробовать еще раз зарегистрироваться, либо отменить регистрацию

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/78b8e8d7-cd2c-45a8-b9a6-ec1b7c136496)

Если пользователь уже пытался зарегистрироваться, но не прошел ее успешно, ему предложат сбросить результаты и снова зарегистрироваться

 ![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/78191bda-420f-49c5-a4d9-ab5193f6d3c5)

После успешной регистрации пользователю предлагается войти в систему. Здесь же добавлена кнопка "зарегистрироваться", на случай, если пользователь ранее не регистрировался
 
![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/369f42ec-f411-45cb-bd05-855c7816105d)

Администатору и менеджерам присылаются письма об успешной регистрации нового пользователя

После успешного входа в систему на панели меню появляются кнопки Создания поста/объявления и кнопка входа на личную страницу пользователя "Me comments", где отображаются отклики к постам/объявлениям пользователя

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/c198a70d-849b-4a3a-b6b8-95d67b0609a7)

Кликнув на название любого поста, пользователь попадает на страницу с полным постом и теперь, после входа в систему, он может писать отклики/ комментарии к постам других пользователей. Но если он зайдет на страницу своего поста, окно с комментарием будет для него недоступно, то есть пользователь может писать комментарии/отклики только к чужим постам

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/f9990e02-cd5f-4624-894e-f0a67d03c0ef)

После того, как он напишет комментарий/ отклик, он отправляется автору поста на рассмотрения, поэтому сразу не появляется на сайте.

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/e1417490-4c60-452f-8830-cab914afe46c)

При этом автору поста приходит уведомление на почту о новом отклике
![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/72bee474-19b1-4f2b-b788-bf568136f77a)

И уведомление автору комментария:

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/3ce519d8-cd5c-4857-b647-33ce8bc766d3)

В личном кабинете My comments  пользователь видит все комментарии к своим постам, если нет комментариев или постов, об этом написано на странице
Здесь пользователь имеет возможность принять или отклонить комментарий/отклик к своему посту/объявлению, а также отфильтровать их по нескольким параметрам

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/e7937b46-9dde-4737-a980-526841158df9)

Если автор поста принял комментарий, то автору комментария приходит уведомление, что комментарий принят

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/eda7a615-2bc9-44e1-9caa-f9a6241591d1)

На всех страницах сайта добавлена удобная навигация, чтобы вернуться на любую страницу сайта. Если пользователь зарегистрирован, на панели меню становится доступной кнопка создания нового поста/лбъявления
При клике на кнопку он переходит на страницу создания поста
Пользователю предлагается выбрать одну из категорий для поста/объявления, вписать название и текст

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/11d784ad-28dd-4708-b492-72f78b615eef)

При клике на значок с картинкой можно вставить картирку в текст
Картинка вставляется как ссылка на нее 

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/76ad806b-88d0-40f1-9c87-e263b3da31a0)

После публикации автору поста приходит уведомление на почту:

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/4724ecf1-e160-4fd4-8aed-d860925720e1)

После публикации поста, если юзер является автором поста, он может его отредактировать или удалить. Сообвествующие кнопки становятся доступны для него на странице поста

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/f4d19095-6b5c-47b3-afea-116e5da91fcf)

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/3d411cef-abc7-4d63-8bd4-963fa25fe2c9)

![image](https://github.com/albinadesign/D16-for-assessment/assets/117900508/e92ace72-488c-4e46-9a00-d482db7709a8)







