#coding: utf-8

import json, gzip, os


def main():
    files_path = ''    
    candidates = ['bolsonaro', 'haddad'] #candidatos
    file_name = 'all_posts' #nome do arquivo com todas as postagens
    
    for candidate in candidates:
        print('********************************************************************************************************')
        print('\t\t\tREADING POSTS FROM %s ' % candidate)
        # caminho para o arquivo de post do candidato
        posts_file_path = '%s%s/%s.json.gz' % (files_path, candidate, file_name)
        # caminho dos comentários
        comments_path = '%s%s/comments/' % (files_path, candidate)
        print('\t\t\t%s' % posts_file_path)
        print('\t\t\t%s' % comments_path)   
        print('********************************************************************************************************')        
        #contador para limitar as postagens exibidas
        posts_count = 0
		
        #carregando o arquivo de postagens compactado
        with gzip.open(posts_file_path) as posts_file:
            for line in posts_file: 
                posts_count+=1
                json_line = json.loads(line.strip())
                post_id = json_line['id']
                print('################################################ POST %d ################################################ \n' % posts_count)                
                print (json_line)
                # verifica se o dicionário contem a chave 'messagem'. Em alguns casos a chave mensagem não está presente
                # no dicionário. Provavelmente porque a postagem não tinha mensagem. Apenas foto ou vídeo.                
                if ('message' in json_line): 
                	print ('\n%s: %s' % (post_id, json_line['message']))
                else:
                	print ('\n%s: campo ausente' % (post_id))	
                
                comments_file_path = '%s%s.json.gz' % (comments_path,post_id)
                
                #verifica se o arquivo de comentários existe
                if not os.path.isfile(comments_file_path):
                    print('<<<<File Not Found>>>>\n')
                    continue
                
                comments_file = gzip.open(comments_file_path)
                comments_count = 0
                for c_line in comments_file:
                    comments_count+=1
                    json_c_line = json.loads(c_line.strip())
                    print('\t<<<<<<<<<<<<<<<<<<<< COMMENT %d >>>>>>>>>>>>>>>>>>>\n' % comments_count)                     
                    print('\t\tcomment %d: %s\n' % (comments_count, json_c_line['message']))
                    print('\t\tnumber_of_likes: %d\n' % (json_c_line['like_count']))                    
                    if comments_count==3:
                        break
                
                if posts_count==2:
                    break
                
        
if __name__ == "__main__":
    main()

